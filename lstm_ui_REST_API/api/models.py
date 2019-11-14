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
    sf = models.CharField(max_length=10, default="simple")
    tv = models.CharField(max_length=10, default="stedy")

    def __str__(self):
        return self.name

class RunningCase(models.Model):
    name = models.IntegerField()
    prefix = models.CharField(max_length=250)
    suffix = models.CharField(max_length=250)

    def __str__(self):
        return self.prefix
