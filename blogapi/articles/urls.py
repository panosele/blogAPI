from django.contrib import admin
from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', views.ArticleRetrieveUpdateDestroyView.as_view(), name='article-detail'),
]