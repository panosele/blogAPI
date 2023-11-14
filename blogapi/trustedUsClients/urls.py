from django.contrib import admin
from django.urls import path
from trustedUsClients import views


urlpatterns = [
    path('trustedUs/', views.TrustedUsClientsListCreateView.as_view(), name='trusted-list-create'),
    path('trustedUs/<int:pk>/', views.TrustedUsClientsRetrieveUpdateDestroyView.as_view(), name='trusted-detail'),
]