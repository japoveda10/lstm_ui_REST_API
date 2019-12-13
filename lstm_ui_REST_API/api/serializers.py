#------------------------------------------------------------------------------
# LSTM UI REST API
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
class EventLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLog
        fields = ['id', 'url', 'name', 'number_of_traces', 'number_of_events', 'number_of_activities', 'avg_activities_per_trace', 'max_activities_per_trace', 'mean_duration', 'max_duration']

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