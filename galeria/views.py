from django.shortcuts import render

from django.http import HttpResponse

from templates import *

from galeria.models import *


def index(request):
    return HttpResponse('<h1> Space</h1><p> Projeto em Django de um site para apresentar imagens do espaço<p>')

def teste(request):
    dados = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards" : dados})

def imagem(request, foto_id):
    fotografia = Fotografia.objects.filter(id=foto_id)
    return render(request, 'galeria/imagem.html', {"foto" : fotografia})