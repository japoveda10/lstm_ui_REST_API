#------------------------------------------------------------------------------
# LSTM UI REST API Project
# By japoveda10
# urls.py
# This file configures the project's urls
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
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
    path('event_logs/', views.EventLogList.as_view()),
    path('event_logs/<int:pk>/', views.EventLogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
