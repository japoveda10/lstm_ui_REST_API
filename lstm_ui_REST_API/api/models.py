from django.db import models

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

    def __str__(self):
        return self.prefix_size

class Activity(models.Model):
    activity_number = models.IntegerField(default=0)
    activity_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.activity_name

# One To Many Table to do match with running case id and activities
# running_case_id
# activity_number

# Event Log, Running Case
# event_log_id
# running_case_id

class Role(models.Model):
    role_id = models.IntegerField(default=0)
    role_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.role_name

class Time(models.Model):
    min = models.IntegerField(default=0)
    max = models.IntegerField(default=0)
    mean = models.IntegerField(default=0)

    def __str__(self):
        return self.mean

# One to Many Activity Role Table
# activity_number
# role_id

# Activity Time Table
# One to one
# Weak entity
# Embedded table