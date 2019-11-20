from rest_framework import serializers
from .models import EventLog, RunningCase, Role, Time

class EventLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLog
        fields = ['id', 'url', 'name', 'number_of_traces', 'number_of_events', 'number_of_activities', 'avg_activities_per_trace', 'max_activities_per_trace', 'mean_duration', 'max_duration']

class RunningCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RunningCase
        fields = ['id', 'prefix_size']

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['role_id', 'role_name']

class TimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Time
        fields = ['min', 'max', 'mean']