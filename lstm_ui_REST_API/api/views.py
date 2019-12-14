#------------------------------------------------------------------------------
# LSTM UI REST API Project
# By japoveda10
# views.py
# This file has classes that represent ViewSets
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
from rest_framework import viewsets
from .models import EventLog, TrainedModel, Result, RunningCase, Activity, Role, Time
from .serializers import EventLogSerializer, TrainedModelSerializer, ResultSerializer, RunningCaseSerializer, ActivitySerializer, RoleSerializer, TimeSerializer

# lstm module
# from lstm import main

#------------------------------------------------------------------------------
# Classes that represent ViewSets
#------------------------------------------------------------------------------

# Event Log ViewSet
class EventLogViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows event logs to be viewed or edited
    '''
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer

# Trained Model ViewSet
class TrainedModelViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows trained models to be viewed or edited
    '''
    queryset = TrainedModel.objects.all()
    serializer_class = TrainedModelSerializer

# Result ViewSet
class ResultViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows results to be viewed or edited
    '''
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

# Running Case ViewSet
class RunningCaseViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows running cases to be viewed or edited
    '''
    queryset = RunningCase.objects.all()
    serializer_class = RunningCaseSerializer
    
    # (1) Detect request (/event_logs/1/running_cases)
    # (2) Call lstm module function
    # main()
    # Data obtained as Python dictionary. Transform it
    # (3) Save data to database

# Activity ViewSet
class ActivityViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows activities to be viewed or edited
    '''
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# Role ViewSet
class RoleViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows roles to be viewed or edited
    '''
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# Time ViewSet
class TimeViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows times to be viewed or edited
    '''
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
