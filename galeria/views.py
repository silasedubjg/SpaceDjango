from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1> Space</h1><p> Projeto em Django de um site para apresentar imagens do espaço<p>')

