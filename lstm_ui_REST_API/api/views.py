#------------------------------------------------------------------------------
# LSTM UI REST API
# viewss.py
# This file has classes that represent viewsets
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
from rest_framework import viewsets
from .models import EventLog, RunningCase, Activity, Role, Time
from .serializers import EventLogSerializer, RunningCaseSerializer, ActivitySerializer, RoleSerializer, TimeSerializer
from backend import hello_world

#------------------------------------------------------------------------------
# Classes that represent viewsets
#------------------------------------------------------------------------------
class EventLogViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows event logs to be viewed or edited
    '''
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer
    hello_world()

    ''' Detect request '''
    ''' Call LSTM project function '''
    ''' Save data to dabase '''

class RunningCaseViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows running cases to be viewed or edited
    '''
    queryset = RunningCase.objects.all()
    serializer_class = RunningCaseSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows activities to be viewed or edited
    '''
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class RoleViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows roles to be viewed or edited
    '''
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class TimeViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows times to be viewed or edited
    '''
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
