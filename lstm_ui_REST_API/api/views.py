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
from rest_framework.response import Response
from rest_framework import status

# lstm module
# from lstm import main

#------------------------------------------------------------------------------
# Classes that represent ViewSets
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

'''# Result ViewSet
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

# Running Case ViewSet
class RunningCaseViewSet(viewsets.ModelViewSet):
    queryset = RunningCase.objects.all()
    serializer_class = RunningCaseSerializer
    
    # (1) Detect request (/event_logs/1/running_cases)
    # (2) Call lstm module function
    # main()
    # Data obtained as Python dictionary. Transform it
    # (3) Save data to database

# Activity ViewSet
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# Role ViewSet
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# Time ViewSet
class TimeViewSet(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer'''
