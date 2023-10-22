from django.shortcuts import render

from django.http import HttpResponse

from templates import *


# Create your views here.

def login(request):
    return render(request, 'usuarios/login.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')
   