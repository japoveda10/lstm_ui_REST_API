#------------------------------------------------------------------------------
# LSTM UI REST API Project
# By japoveda10
# urls.py
# This file configures the project's urls
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
import os

from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from api import views

#------------------------------------------------------------------------------
# Router
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# URL Patterns
#------------------------------------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api_root),
    path('event_logs/', views.EventLogList.as_view(), name='event_log-list'),
    path('event_logs/<int:pk>/', views.EventLogDetail.as_view()),
    path('event_logs/<int:pk>/running_cases/', views.RunningCaseList.as_view()),
    path('event_logs/<int:pk1>/running_cases/<int:pk2>', views.RunningCaseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

print("Ready to execute event_log_services.py")
os.system("python event_log_services.py")
print("Finished executing event_log_services.py")
