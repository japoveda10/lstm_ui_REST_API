from rest_framework import viewsets
from .models import EventLog, RunningCase
from .serializers import EventLogSerializer, RunningCaseSerializer

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
