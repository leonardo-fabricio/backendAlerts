from os import path
from django.urls import  path
from backendAlerts.api.views import AlertCreate, AlertList

urlpatterns = [
     path('create-alert/',AlertCreate.as_view(), name='create-alert'),
     path('list-alert/', AlertList.as_view(), name='list-alert')
]