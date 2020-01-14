# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 16:11:48 2019

@author: Manuel Camargo
"""

import os
import random
import itertools
from operator import itemgetter
import uuid

import pandas as pd
import numpy as np

from support_modules.readers import log_reader as lr
from support_modules import role_discovery as rl
from support_modules import nn_support as nsup

def load_event_log(parms):
    # Dataframe creation
    # Filter load local inter-case features or filter them
    log = lr.LogReader(os.path.join('input_files', parms['file_name']), parms['read_options'])
    log_df = pd.DataFrame(log.data)
    # Resource pool discovery
    _, resource_table = rl.read_resource_pool(log_df, sim_percentage=parms['rp_similarity'], dataframe=True)
    # Role discovery
    log_df_resources = pd.DataFrame.from_records(resource_table)
    log_df_resources = log_df_resources.rename(index=str, columns={"resource": "user"})
    # Dataframe creation
    log_df = log_df.merge(log_df_resources, on='user', how='left')
    log_df = log_df.reset_index(drop=True)
    log_df = add_calculated_features(log_df, parameters)
    statistics = calculate_event_log_statistics(log_df, parms)
    #TODO: other fields are missing like the route in the server or storage
    statistics['name'] = parms['file_name']
    return statistics, log_df

def calculate_event_log_statistics(log_df, parms):
    # Analysis of start tasks
    ordering_field = 'start_timestamp'
    if parms['read_options']['one_timestamp']:
        ordering_field = 'end_timestamp'

    activities = log_df.task.unique()
    roles = log_df.role.unique()

    stats_df = (pd.DataFrame(log_df.groupby('caseid')[ordering_field]
                                        .agg(['min', 'max', 'count'])
                                              .reset_index()))
    stats_df['count'] = pd.to_numeric(stats_df['count'], downcast='float')
    stats_df['cycle_time'] = stats_df['max'] - stats_df['min']
    stats = {
        'mean_activities_per_trace':np.mean(stats_df['count']),
        'min_activities_per_trace':np.min(stats_df['count']),
        'max_activities_per_trace':np.max(stats_df['count']),
        'mean_cycle_time':np.mean(stats_df['cycle_time']),
        'min_cycle_time':np.min(stats_df['cycle_time']),
        'max_cycle_time':np.max(stats_df['cycle_time']),
        'number_of_activities': len(activities),
        'number_of_roles': len(roles),
        'number_of_events':np.sum(stats_df['count']),
        'number_of_traces':len(stats_df)
        }

    return stats

def create_activities_table(log_df):
    activities_table = log_df[['dur','task']].groupby(['task']).agg(['min','max','mean']).reset_index()
    activities_table.columns = activities_table.columns.droplevel(0)
    activities_table = activities_table.rename(index=str, columns={'': "activity_name"})
    row=pd.DataFrame([{'activity_name':'start','min':0,'max':0,'mean':0},
                      {'activity_name':'end','min':0,'max':0,'mean':0}])
    activities_table = activities_table.append(row, ignore_index=True, sort=True)
    activities_table['id']= activities_table.apply(gen_id, prefix='AC',axis=1)
    index = create_index(log_df, 'task')
    index = pd.DataFrame.from_dict(index, orient='index', columns=['activity_number']).reset_index().rename(columns={"index": 'activity_name'})
    activities_table = activities_table.merge(index, on='activity_name', how='left')
    activities_table = activities_table.set_index('id')
    return activities_table

def create_roles_table(log_df):
    roles_table = create_index(log_df, 'role')
    roles_table = pd.DataFrame.from_dict(roles_table, orient='index', columns=['role_number']).reset_index().rename(columns={"index": 'role_name'})
    roles_table['id']= roles_table.apply(gen_id, prefix='RL', axis=1)
    roles_table = roles_table.set_index('id')
    return roles_table

    
def generate_running_cases(log_df, activities_table, roles_table, parms):
    log_df = log_df.merge(activities_table[['activity_name','activity_number']], left_on='task',right_on='activity_name', how='left')
    log_df = log_df.merge(roles_table[['role_name','role_number']], left_on='role',right_on='role_name', how='left')
    log_df = log_df.drop(columns=['activity_name', 'role_name'])
    equi = {'activity_number':'activities', 'role_number':'roles', 'dur_norm':'times'}
    log_df = nsup.scale_feature(log_df, 'dur', parms['norm_method'])
    columns = list(equi.keys())
    
    full_prefixes = {'max_dur':np.max(log_df.dur)}
    log_df = reformat_events(log_df, activities_table, roles_table, columns, parameters)
#    max_length = np.max([len(x['ac_index']) for x in log_df])
    # n-gram definition
    for i, _ in enumerate(log_df):
        for x in columns:
            serie = list()
            for idx in range(1, len(log_df[i][x])):
#                serie.append([0]*(max_length - idx) + log_df[i][x][:idx])
                serie.append(log_df[i][x][:idx])
            full_prefixes[equi[x]] = full_prefixes[equi[x]] + serie if i > 0 else serie

    ac_alias = create_alias(len(activities_table))
    rl_alias = create_alias(len(roles_table))
    # all examples
    all_prefixes = list()
    for i,_ in enumerate(full_prefixes['activities']):
        all_prefixes.append({
                'activities_serie':full_prefixes['activities'][i],
                'roles_serie':full_prefixes['roles'][i],
                'activities_hash':hash(''.join([ac_alias[x] for x in full_prefixes['activities'][i]])),
                'roles_hash':hash(''.join([rl_alias[x] for x in full_prefixes['roles'][i]]))
                })
    return all_prefixes

def create_series_table(all_prefixes, attr, attr1,table, pr):
    attribute = dict()
    attribute_series = list()
    for prefix in all_prefixes:
        if prefix[attr+'_hash'] not in attribute.keys():
            id_num = gen_id('', pr)
            attribute[prefix[attr+'_hash']] = [len(prefix[attr+'_serie']), id_num]
            for number in prefix[attr+'_serie']:
                attribute_series.append({
                        'seq_id': id_num,
                        attr+'_hash':prefix[attr+'_hash'],
                        'number': number
                    })
    attribute = pd.DataFrame.from_dict(attribute, orient='index', columns=['seq_size', 'id'])
    attribute_series = pd.DataFrame(attribute_series)
    attribute_series = attribute_series.merge(table[[attr1+'_number']].reset_index(), left_on='number', right_on=attr1+'_number', how='left')
    attribute_series = attribute_series.drop(columns=[attr+'_hash',attr1+'_number', 'number'])
    return attribute, attribute_series

def create_running_case(all_prefixes, activities, roles):
    runing_cases = pd.DataFrame(all_prefixes)
    runing_cases = runing_cases[['activities_hash', 'roles_hash']].drop_duplicates()
    runing_cases = runing_cases.merge(activities[['id']].reset_index(), left_on='activities_hash', right_on='index', how='left')
    runing_cases = runing_cases.drop(columns=['activities_hash', 'index'])
    runing_cases = runing_cases.rename(index=str, columns={"id": "activities_id"})
    runing_cases = runing_cases.merge(roles[['id']].reset_index(), left_on='roles_hash', right_on='index', how='left')
    runing_cases = runing_cases.drop(columns=['roles_hash', 'index'])
    runing_cases = runing_cases.rename(index=str, columns={"id": "roles_id"})
    
    activities = activities.reset_index().drop(columns=['index']).set_index('id')
    roles = roles.reset_index().drop(columns=['index']).set_index('id')

    return runing_cases, activities, roles

# =============================================================================
# Support methods
# =============================================================================
def reformat_events(log_df, ac_table, rl_table, columns, parms):
    """Creates series of activities, roles and relative times per trace.
    parms:
        log_df: dataframe.
        ac_table (dict): index of activities.
        rl_table (dict): index of roles.
    Returns:
        list: lists of activities, roles and relative times.
    """
    temp_data = list()
    log_df = log_df.to_dict('records')
    if parms['read_options']['one_timestamp']:
        log_df = sorted(log_df, key=lambda x: (x['caseid'], x['end_timestamp']))
    else:
        log_df = sorted(log_df, key=lambda x: (x['caseid'], x['start_timestamp']))
    for key, group in itertools.groupby(log_df, key=lambda x: x['caseid']):
        trace = list(group)
        temp_dict = dict()
        for x in columns:
            serie = [y[x] for y in trace]
            if x == 'ac_table':
                serie.insert(0, ac_table[ac_table.activity_name == 'start'].iloc[-1]['activity_number'])
                serie.append(ac_table[ac_table.activity_name == 'end'].iloc[-1]['activity_number'])
            elif x == 'rl_table':
                serie.insert(0, rl_table[rl_table.role_name == 'start'].iloc[-1]['role_number'])
                serie.append(rl_table[rl_table.role_name == 'end'].iloc[-1]['role_number'])
            else:
                serie.insert(0, 0)
                serie.append(0)
            temp_dict = {**{x: serie},**temp_dict}
        temp_dict = {**{'caseid': key},**temp_dict}
        temp_data.append(temp_dict)
    return temp_data

def create_index(log_df, column):
    """Creates an idx for a categorical attribute.
    parms:
        log_df: dataframe.
        column: column name.
    Returns:
        index of a categorical attribute pairs.
    """
    temp_list = log_df[[column]].values.tolist()
    subsec_set = {(x[0]) for x in temp_list}
    subsec_set = sorted(list(subsec_set))
    alias = dict()
    for i, _ in enumerate(subsec_set):
        alias[subsec_set[i]] = i + 1
    alias['start'] = 0
    alias['end'] = len(alias)
    return alias

def create_alias(quantity):
    """Creates char aliases for a categorical attributes.
    Args:
        quantity (int): number of aliases to create.
    Returns:
        dict: alias for a categorical attributes.
    """
    characters = [chr(i) for i in range(0, quantity)]
    aliases = random.sample(characters, quantity)
    alias = dict()
    for i in range(0, quantity):
        alias[i] = aliases[i]
    return alias

def add_calculated_features(log_df, parms):
    """Appends the indexes and relative time to the dataframe.
    parms:
        log_df: dataframe.
        ac_index (dict): index of activities.
        rl_index (dict): index of roles.
    Returns:
        Dataframe: The dataframe with the calculated features added.
    """
    log_df['dur'] = 0

    log_df = log_df.to_dict('records')
    if parms['read_options']['one_timestamp']:
        log_df = sorted(log_df, key=lambda x: x['caseid'])
        for key, group in itertools.groupby(log_df, key=lambda x: x['caseid']):
            events = list(group)
            events = sorted(events, key=itemgetter('end_timestamp'))
            for i in range(0, len(events)):
                # In one-timestamp approach the first activity of the trace is taken as instant
                # since there is no previous timestamp to find a range
                if i == 0:
                    events[i]['dur'] = 0
                else:
                    dur = (events[i]['end_timestamp']-events[i-1]['end_timestamp']).total_seconds()
                    events[i]['dur'] = dur
    else:
        log_df = sorted(log_df, key=itemgetter('start_timestamp'))
        for event in log_df:
            # on the contrary is btw start and complete timestamp
            event['dur']=(event['end_timestamp'] - event['start_timestamp']).total_seconds()
    return pd.DataFrame.from_dict(log_df)


def gen_id(x, prefix):
    return prefix + str(uuid.uuid4())

# =============================================================================
# Kernel
# This will be removed after integration
# The next parameters need to be defined to perform the query
# =============================================================================

parameters = dict()

# Matching between the csv columns and the event log
column_names = {'Case ID':'caseid', 'Activity':'task',
                'lifecycle:transition':'event_type', 'Resource':'user'}
# Parameters for event-log reading
parameters['read_options'] = {'timeformat': '%Y-%m-%dT%H:%M:%S.%f',
                              'column_names':column_names,
                              'one_timestamp': False,
                              'reorder':False,
                              'ns_include':True,
                              'filter_d_attrib':True}
parameters['file_name'] = 'ConsultaDataMining201618.xes.gz'
# Similarity btw the resources profile execution (Song e.t. all)
parameters['rp_similarity'] = 0.8
# Normalization method
parameters['norm_method'] = 'max' # max, lognorm

#load event log and statistics
statistics, log_df = load_event_log(parameters)
print(statistics)
# Activities table
activities_table = create_activities_table(log_df)
roles_table = create_roles_table(log_df)
print(activities_table)
print(activities_table.dtypes)
print(roles_table)
# transformation in sequences
all_prefixes = generate_running_cases(log_df, activities_table, roles_table, parameters)
# Sequences tables
activities ,activities_series = create_series_table(all_prefixes, 'activities', 'activity', activities_table, 'ACSQ')
roles ,roles_series = create_series_table(all_prefixes, 'roles', 'role', roles_table, 'RLSQ')
# running cases
runing_cases, activities, roles = create_running_case(all_prefixes, activities, roles)
print(activities)
print(activities_series)
print(roles)
print(roles_series)
print(runing_cases)
