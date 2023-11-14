from rest_framework import serializers
from .models import NewsLetter

class NewsLetterClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = ["id", "message", "name", "surname", "email", "date"]