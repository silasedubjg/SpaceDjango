from django.shortcuts import render

from django.http import HttpResponse

from templates import *

from usuarios.forms import LoginForm


# Create your views here.

def login(request):
    form= LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')
   