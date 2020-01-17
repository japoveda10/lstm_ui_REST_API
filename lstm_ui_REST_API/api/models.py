#------------------------------------------------------------------------------
# LSTM UI REST API Project
# By japoveda10
# models.py
# This file has classes that represent models
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
from django.db import models

#------------------------------------------------------------------------------
# Classes that represent models
#------------------------------------------------------------------------------

# Event Log Model
class EventLog(models.Model):
    name = models.CharField(max_length=50)
    number_of_traces = models.IntegerField(default=0)
    number_of_events = models.IntegerField(default=0)
    number_of_activities = models.IntegerField(default=0)
    avg_activities_per_trace = models.FloatField(default=0)
    max_activities_per_trace = models.FloatField(default=0)
    mean_duration = models.CharField(max_length=100, default="0 days")
    max_duration = models.CharField(max_length=100, default="0 days")
    roles = models.ManyToManyField('Role')
    activities = models.ManyToManyField('Activity')

    def __str__(self):
        return self.name

# Trained Model Model
class TrainedModel(models.Model):
    running_case = models.ForeignKey(EventLog, default="", on_delete=models.CASCADE)
    accuracy = models.FloatField(default=0)

    def __str__(self):
        return self.accuracy

# Result Model
class Result(models.Model):
    trained_model = models.ForeignKey(TrainedModel, default="", on_delete=models.CASCADE)
    mae = models.FloatField(default=0)
    similarity = models.FloatField(default=0)
    distance = models.FloatField(default=0)
    prefix_size = models.IntegerField(default=0)

    def __str__(self):
        return self.mae

# Role Sequence Model
class RoleSequence(models.Model):
    sequence_id = models.IntegerField(default=0)
    other_id = models.IntegerField(default=0)

    def __str__(self):
        return self.role_name

# Activity Sequence Model
class ActivitySequence(models.Model):
    sequence_id = models.IntegerField(default=0)
    other_id = models.IntegerField(default=0)
    roles = models.ManyToManyField('Role')

    def __str__(self):
        return self.role_name

# Running Case Model
class RunningCase(models.Model):
    prefix_size = models.IntegerField(default=0)
    #event_log = models.ForeignKey('EventLog', default="", on_delete=models.CASCADE)
    event_log_name = models.ForeignKey('EventLog', db_column='name', default="", on_delete=models.CASCADE)
    #event_log_name = models.CharField(max_length=100, default="0 days")
    role_sequence_id = models.ForeignKey(RoleSequence, default="", on_delete=models.CASCADE)
    activity_sequence_id = models.ForeignKey(ActivitySequence, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.prefix_size

# Activity Model
class Activity(models.Model):
    activity_number = models.IntegerField(default=0)
    activity_name = models.CharField(max_length=100, default="")
    activity_sequence = models.ForeignKey(ActivitySequence, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.activity_name

# Role Model
class Role(models.Model):
    role_id = models.IntegerField(default=0)
    role_name = models.CharField(max_length=100, default="")
    role_sequence = models.ForeignKey(RoleSequence, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.role_name
