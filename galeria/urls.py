from django.contrib import admin
from django.urls import path
from galeria.views import *

urlpatterns = [
    path('', index),
    path('teste', teste)
]
