from django.urls import path
from django.shortcuts import render
from .views import *

urlpatterns = [
    path('',home),
    path('register',registration,name='register'),
]
