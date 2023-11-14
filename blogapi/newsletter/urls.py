from django.contrib import admin
from django.urls import path
from newsletter import views


urlpatterns = [
    path('newsletter/', views.NewsLetterClientsListCreateView.as_view(), name='newsletter-list-create'),
    path('newsletter/<int:pk>/', views.NewsLetterClientsRetrieveUpdateDestroyView.as_view(), name='newsletter-detail'),
]