#------------------------------------------------------------------------------
# LSTM UI REST API Project
# By japoveda10
# serializers.py
# This file has classes that represent serializers
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
from rest_framework import serializers
from .models import EventLog, TrainedModel, Result, RunningCase, Activity, Role, Time

#------------------------------------------------------------------------------
# Classes that represent serializers
#------------------------------------------------------------------------------

# Event Log Serializer
class EventLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    number_of_traces = serializers.IntegerField(required=True)
    number_of_events = serializers.IntegerField(required=True)
    number_of_activities = serializers.IntegerField(required=True)
    avg_activities_per_trace = serializers.FloatField(required=True)
    max_activities_per_trace = serializers.FloatField(required=True)
    mean_duration = serializers.CharField(required=True, allow_blank=False, max_length=100)
    max_duration = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `EventLog` instance, given the validated data.
        """
        return EventLog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `EventLog` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.number_of_traces = validated_data.get('number_of_traces', instance.number_of_traces)
        instance.number_of_events = validated_data.get('number_of_events', instance.number_of_events)
        instance.number_of_activities = validated_data.get('number_of_activities', instance.number_of_activities)
        instance.avg_activities_per_trace = validated_data.get('avg_activities_per_trace', instance.avg_activities_per_trace)
        instance.max_activities_per_trace = validated_data.get('max_activities_per_trace', instance.max_activities_per_trace)
        instance.mean_duration = validated_data.get('mean_duration', instance.mean_duration)
        instance.max_duration = validated_data.get('max_duration', instance.max_duration)
        instance.save()
        return instance

# Trained Model Serializer
class TrainedModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainedModel
        fields = ['id', 'url', 'running_case', 'accuracy']

# Result Serializer
class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'url', 'trained_model', 'mae', 'similarity', 'distance', 'prefix_size']

# Running Case Serializer
class RunningCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RunningCase
        fields = ['id', 'url', 'prefix_size', 'event_log']

# Activity Serializer
class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'url', 'activity_number', 'activity_name', 'running_case']

# Role Serializer
class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'url', 'role_id', 'role_name', 'activity']

# Time Serializer
class TimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Time
        fields = ['id', 'url', 'min', 'max', 'mean', 'activity']