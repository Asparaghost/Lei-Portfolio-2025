from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('projects/<str:proj_hash>/', views.proj_info, name='proj_info'),
]