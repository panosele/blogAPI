from rest_framework import serializers
from .models import TrustedUsClients

class TrustedUsClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustedUsClients
        fields = ["id", "title", "image", "date"]