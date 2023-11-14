from django.shortcuts import render
from rest_framework import generics
from .models import NewsLetter
from .serializers import NewsLetterClientsSerializer
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse



class NewsLetterClientsListCreateView(generics.ListCreateAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterClientsSerializer

    # if generics.ListCreateAPIView.queryset:
    #     queryset = generics.ListCreateAPIView.queryset
    #     try:
    #         send_mail(queryset.name, queryset.message, queryset.email, ["panosfps1993@gmail.com"])
    #         HttpResponse("Success")
    #     except BadHeaderError:
    #         HttpResponse("Invalid header found.")
		


    

class NewsLetterClientsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterClientsSerializer
