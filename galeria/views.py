from django.shortcuts import render

from django.http import HttpResponse

from templates import *



def index(request):
    return HttpResponse('<h1> Space</h1><p> Projeto em Django de um site para apresentar imagens do espaço<p>')

def teste(request):
    dados = {
        1:{ "nome" : "Nebulosa de Órion",
            "creditos": "Nasa.org / Nasa / Hubble"},
        2:{ "nome" : "Os pilares da criação",
            "creditos": "Nasa.org / Nasa / Jeff Hester"},
    }
    return render(request, 'galeria/index.html', {"cards" : dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')