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
from .models import EventLog, TrainedModel, Result, RunningCase, Activity, ActivitySequence, Role, RoleSequence

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

# Running Case Serializer
class RunningCaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    prefix_size = serializers.IntegerField(required=True)
    event_log = EventLogSerializer(many=True)

    def create(self, validated_data):
        """
        Create and return a new `RunningCase` instance, given the validated data.
        """
        return RunningCase.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `RunningCase` instance, given the validated data.
        """
        instance.prefix_size = validated_data.get('prefix_size', instance.prefix_size)
        instance.event_log = validated_data.get('event_log', instance.event_log)
        instance.save()
        return instance

# Trained Model Serializer
class TrainedModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    running_case = RunningCaseSerializer(many=True)
    accuracy = serializers.FloatField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `TrainedModel` instance, given the validated data.
        """
        return TrainedModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `TrainedModel` instance, given the validated data.
        """
        instance.running_case = validated_data.get('running_case', instance.running_case)
        instance.accuracy = validated_data.get('accuracy', instance.accuracy)
        instance.save()
        return instance

# Result Serializer
class ResultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    trained_model = TrainedModelSerializer(many=True)
    mae = serializers.FloatField(required=True)
    similarity = serializers.FloatField(required=True)
    distance = serializers.FloatField(required=True)
    prefix_size = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Result` instance, given the validated data.
        """
        return Result.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Result` instance, given the validated data.
        """
        instance.trained_model = validated_data.get('trained_model', instance.trained_model)
        instance.mae = validated_data.get('mae', instance.mae)
        instance.similarity = validated_data.get('similarity', instance.similarity)
        instance.distance = validated_data.get('distance', instance.distance)
        instance.prefix_size = validated_data.get('prefix_size', instance.prefix_size)
        instance.save()
        return instance

# Activity Serializer
class ActivitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    activity_number = serializers.IntegerField(required=True)
    activity_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    running_case = RunningCaseSerializer(many=True)

    def create(self, validated_data):
        """
        Create and return a new `Activity` instance, given the validated data.
        """
        return Activity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Activity` instance, given the validated data.
        """
        instance.activity_number = validated_data.get('activity_number', instance.activity_number)
        instance.activity_name = validated_data.get('activity_name', instance.activity_name)
        instance.running_case = validated_data.get('running_case', instance.running_case)
        instance.save()
        return instance

# Activity Sequence Serializer
class ActivitySequenceSerializer(serializers.Serializer):
    sequence_id = serializers.IntegerField(required=True)
    other_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `ActivitySequence` instance, given the validated data.
        """
        return ActivitySequence.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `ActivitySequence` instance, given the validated data.
        """
        instance.sequence_id = validated_data.get('sequence_id', instance.sequence_id)
        instance.other_id = validated_data.get('other_id', instance.other_id)
        instance.save()
        return instance

# Role Serializer
class RoleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    role_id = serializers.IntegerField(required=True)
    role_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    activity = ActivitySerializer(many=True)

    def create(self, validated_data):
        """
        Create and return a new `Role` instance, given the validated data.
        """
        return Role.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Role` instance, given the validated data.
        """
        instance.role_id = validated_data.get('role_id', instance.role_id)
        instance.role_name = validated_data.get('role_name', instance.role_name)
        instance.activity = validated_data.get('activity', instance.activity)
        instance.save()
        return instance

# Role Sequence Serializer
class RoleSequenceSerializer(serializers.Serializer):
    sequence_id = serializers.IntegerField(required=True)
    other_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `RoleSequence` instance, given the validated data.
        """
        return RoleSequence.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `RoleSequence` instance, given the validated data.
        """
        instance.sequence_id = validated_data.get('sequence_id', instance.sequence_id)
        instance.other_id = validated_data.get('other_id', instance.other_id)
        instance.save()
        return instance
