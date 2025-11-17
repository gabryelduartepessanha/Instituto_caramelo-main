from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_ong/', views.registrar_ong, name='registrar_ong'),
    path("parceiros/", views.parceiros, name="parceiros"),
]
