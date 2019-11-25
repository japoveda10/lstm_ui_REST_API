#------------------------------------------------------------------------------
# LSTM UI REST API
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
class EventLog(models.Model):
    name = models.CharField(max_length=50)
    number_of_traces = models.IntegerField(default=0)
    number_of_events = models.IntegerField(default=0)
    number_of_activities = models.IntegerField(default=0)
    avg_activities_per_trace = models.FloatField(default=0)
    max_activities_per_trace = models.FloatField(default=0)
    mean_duration = models.CharField(max_length=100, default="0 days")
    max_duration = models.CharField(max_length=100, default="0 days")

    def __str__(self):
        return self.name

class RunningCase(models.Model):
    prefix_size = models.IntegerField(default=0)
    event_log = models.ForeignKey(EventLog, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.prefix_size

class Activity(models.Model):
    activity_number = models.IntegerField(default=0)
    activity_name = models.CharField(max_length=100, default="")
    running_case = models.ForeignKey(RunningCase, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.activity_name

class Role(models.Model):
    role_id = models.IntegerField(default=0)
    role_name = models.CharField(max_length=100, default="")
    activity = models.ForeignKey(Activity, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.role_name

class Time(models.Model):
    min = models.IntegerField(default=0)
    max = models.IntegerField(default=0)
    mean = models.IntegerField(default=0)
    activity = models.OneToOneField(Activity, default="", on_delete = models.CASCADE)

    def __str__(self):
        return self.mean
