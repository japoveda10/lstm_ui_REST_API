#------------------------------------------------------------------------------
# LSTM UI REST API Project
# By japoveda10
# views.py
# This file has classes that represent ViewSets
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
from .models import EventLog, TrainedModel, Result, RunningCase, Activity, Role, Time
from .serializers import EventLogSerializer, TrainedModelSerializer, ResultSerializer, RunningCaseSerializer, ActivitySerializer, RoleSerializer, TimeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

# lstm module
# from lstm import main

#------------------------------------------------------------------------------
# API Root
#------------------------------------------------------------------------------

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'event_logs': reverse('event_log-list', request=request, format=format),
    })

#------------------------------------------------------------------------------
# Classes that represent API Views
#------------------------------------------------------------------------------

# Event Log List
class EventLogList(APIView):
    """
    List all event logs, or create a new event log
    """
    def get(self, request, format=None):
        print("GET event logs")
        event_logs = EventLog.objects.all()
        serializer = EventLogSerializer(event_logs, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("POST event logs")
        serializer = EventLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Event Log Detail
class EventLogDetail(APIView):
    """
    Retrieve, update or delete an event log instance
    """
    def get_object(self, pk):
        try:
            return EventLog.objects.get(pk=pk)
        except EventLog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("GET specific event log")
        event_log = self.get_object(pk)
        serializer = EventLogSerializer(event_log)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        print("UPDATE specific event log")
        event_log = self.get_object(pk)
        serializer = EventLogSerializer(event_log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print("DELTE specific event log")
        event_log = self.get_object(pk)
        event_log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Trained Model List
class TrainedModelList(APIView):
    """
    List all trained models, or create a new trained model
    """
    def get(self, request, format=None):
        print("GET trained models")
        trained_models = TrainedModel.objects.all()
        serializer = TrainedModelSerializer(trained_models, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("POST trained models")
        serializer = TrainedModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Trained Model Detail
class TrainedModelDetail(APIView):
    """
    Retrieve, update or delete a trained model instance
    """
    def get_object(self, pk):
        try:
            return TrainedModel.objects.get(pk=pk)
        except TrainedModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("GET specific trained model")
        trained_model = self.get_object(pk)
        serializer = TrainedModelSerializer(trained_model)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        print("UPDATE specific trained model")
        trained_model = self.get_object(pk)
        serializer = TrainedModelSerializer(trained_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print("DELTE specific trained model")
        trained_model = self.get_object(pk)
        trained_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Result List
class ResultList(APIView):
    """
    List all results, or create a new result
    """
    def get(self, request, format=None):
        print("GET results")
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("POST results")
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Result Detail
class ResultDetail(APIView):
    """
    Retrieve, update or delete a result instance
    """
    def get_object(self, pk):
        try:
            return Result.objects.get(pk=pk)
        except Result.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("GET specific result")
        result = self.get_object(pk)
        serializer = ResultSerializer(result)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        print("UPDATE specific result")
        result = self.get_object(pk)
        serializer = EventLogSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print("DELTE specific result")
        result = self.get_object(pk)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Running Case List
class RunningCaseList(APIView):
    """
    List all running cases, or create a new running case
    """
    def get(self, request, format=None):
        print("GET running cases")
        running_cases = RunningCase.objects.all()
        serializer = RunningCaseSerializer(running_cases, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("POST running cases")
        serializer = RunningCaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Running Case Detail
class RunningCaseDetail(APIView):
    """
    Retrieve, update or delete a running case instance
    """
    def get_object(self, pk):
        try:
            return RunningCase.objects.get(pk=pk)
        except RunningCase.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("GET specific running case")
        running_case = self.get_object(pk)
        serializer = RunningCaseSerializer(running_case)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        print("UPDATE specific running case")
        running_case = self.get_object(pk)
        serializer = RunningCaseSerializer(running_case, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print("DELTE specific running case")
        running_case = self.get_object(pk)
        running_case.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Activity List
class ActivityList(APIView):
    """
    List all activities, or create a new activity
    """
    def get(self, request, format=None):
        print("GET activities")
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("POST activities")
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Activity Detail
class ActivityDetail(APIView):
    """
    Retrieve, update or delete an activity instance
    """
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("GET specific activity")
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        print("UPDATE specific activity")
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print("DELTE specific activity")
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Role List
class RoleList(APIView):
    """
    List all roles, or create a new role
    """
    def get(self, request, format=None):
        print("GET roles")
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("POST roles")
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Role Detail
class RoleDetail(APIView):
    """
    Retrieve, update or delete a role instance
    """
    def get_object(self, pk):
        try:
            return Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("GET specific role")
        role = self.get_object(pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        print("UPDATE specific role")
        role = self.get_object(pk)
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print("DELTE specific role")
        role = self.get_object(pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Time List
class TimeList(APIView):
    """
    List all times, or create a new time
    """
    def get(self, request, format=None):
        print("GET times")
        times = Time.objects.all()
        serializer = TimeSerializer(roles, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("POST times")
        serializer = TimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Time Detail
class TimeDetail(APIView):
    """
    Retrieve, update or delete a time instance
    """
    def get_object(self, pk):
        try:
            return Time.objects.get(pk=pk)
        except Time.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("GET specific time")
        time = self.get_object(pk)
        serializer = TimeSerializer(time)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        print("UPDATE specific time")
        time = self.get_object(pk)
        serializer = TimeSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print("DELTE specific time")
        role = self.get_object(pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

