from django.contrib import admin
from django.urls import path
from apps.galeria.views import *

urlpatterns = [
    path('', index),
    path('teste', teste, name='Home'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
    path('addimagem/', adicionarimagem, name='addimagem'),
    path('deletarimagem/', deletarimagem, name='deletarimagem'),
    path('editarimagem/', editarimagem, name='editarimagem'),
]
