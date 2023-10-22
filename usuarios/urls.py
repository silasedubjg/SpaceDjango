from django.contrib import admin
from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
]
