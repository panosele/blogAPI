from django.contrib import admin
from django.urls import path
from bannersAdds import views


urlpatterns = [
    path('banners/', views.BannerListCreateView.as_view(), name='banner-list-create'),
    path('banners/<int:pk>/', views.BannerRetrieveUpdateDestroyView.as_view(), name='banner-detail'),
]