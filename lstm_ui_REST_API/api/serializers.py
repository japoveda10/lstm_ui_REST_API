from rest_framework import serializers
from .models import EventLog, RunningCase

class EventLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLog
        fields = ['id', 'url', 'name', 'number_of_traces', 'number_of_events', 'number_of_activities', 'avg_activities_per_trace', 'max_activities_per_trace', 'mean_duration', 'max_duration', 'sf', 'tv']

class RunningCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RunningCase
        fields = ['id', 'name', 'prefix', 'suffix']