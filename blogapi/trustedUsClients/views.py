from django.shortcuts import render
from rest_framework import generics
from .models import TrustedUsClients
from .serializers import TrustedUsClientsSerializer

class TrustedUsClientsListCreateView(generics.ListCreateAPIView):
    queryset = TrustedUsClients.objects.all()
    serializer_class = TrustedUsClientsSerializer

class TrustedUsClientsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrustedUsClients.objects.all()
    serializer_class = TrustedUsClientsSerializer