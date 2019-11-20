from rest_framework import viewsets
from .models import EventLog, RunningCase, Role, Time
from .serializers import EventLogSerializer, RunningCaseSerializer, RoleSerializer, TimeSerializer

class EventLogViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows event logs to be viewed or edited
    '''
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer

class RunningCaseViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows running cases to be viewed or edited
    '''
    queryset = RunningCase.objects.all()
    serializer_class = RunningCaseSerializer

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
