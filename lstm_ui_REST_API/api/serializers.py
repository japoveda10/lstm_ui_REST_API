#------------------------------------------------------------------------------
# LSTM UI REST API
# serializers.py
# This file has classes that represent serializers
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
from rest_framework import serializers
from .models import EventLog, RunningCase, Activity, Role, Time

#------------------------------------------------------------------------------
# Classes that represent serializers
#------------------------------------------------------------------------------
class EventLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLog
        fields = ['id', 'url', 'name', 'number_of_traces', 'number_of_events', 'number_of_activities', 'avg_activities_per_trace', 'max_activities_per_trace', 'mean_duration', 'max_duration']

class RunningCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RunningCase
        fields = ['id', 'url', 'prefix_size', 'event_log']

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'url', 'activity_number', 'activity_name', 'running_case']

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'url', 'role_id', 'role_name', 'activity']

class TimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Time
        fields = ['id', 'url', 'min', 'max', 'mean', 'activity']