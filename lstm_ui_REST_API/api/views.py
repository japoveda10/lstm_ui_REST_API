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

# Event Log ViewSet
class EventLogList(APIView):
    def get(self, request, format=None):
        print("GET eventlogs")
        event_logs = EventLog.objects.all()
        serializer = EventLogSerializer(event_logs, many=True)
        return Response(serializer.data)

class EventLogDetail(APIView):
    """
    Retrieve, update or delete an event log instance.
    """
    def get_object(self, pk):
        try:
            return EventLog.objects.get(pk=pk)
        except EventLog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event_log = self.get_object(pk)
        serializer = EventLogSerializer(event_log)
        return Response(serializer.data)

# Trained Model ViewSet
'''class TrainedModelViewSet(viewsets.ModelViewSet):
    queryset = TrainedModel.objects.all()
    serializer_class = TrainedModelSerializer

# Result ViewSet
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
