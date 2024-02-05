from rest_framework import routers, serializers, viewsets
from backendAlerts.models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields ='__all__'
