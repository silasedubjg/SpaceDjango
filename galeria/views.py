from django.shortcuts import render

from django.http import HttpResponse

from templates import *

def index(request):
    return HttpResponse('<h1> Space</h1><p> Projeto em Django de um site para apresentar imagens do espaço<p>')

def teste(request):
    return render(request, 'home.html')
