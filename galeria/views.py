from django.shortcuts import render, redirect

from django.http import HttpResponse

from templates import *

from galeria.models import *


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    dados = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards" : dados})

def teste(request):
    if not request.user.is_authenticated:
        return redirect('login')
    dados = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards" : dados})

def imagem(request, foto_id):
    if not request.user.is_authenticated:
        return redirect('login')
    fotografia = Fotografia.objects.filter(id=foto_id)
    return render(request, 'galeria/imagem.html', {"foto" : fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        return redirect('login')
    fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        tag = request.GET['buscar']
        if tag:
            fotografia = fotografia.filter(nome__icontains=tag)
    return render(request, 'galeria/buscar.html', {"cards" : fotografia})
