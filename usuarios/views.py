from django.shortcuts import render, redirect

from django.http import HttpResponse

from templates import *

from usuarios.forms import LoginForm, cadastroForm

from django.contrib.auth.models import User
# Create your views here.

def login(request):
    form= LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = cadastroForm()

    if request.method == 'POST':
        form = cadastroForm(request.POST)

        if form.is_valid:
            if form['senha'].value != form['senha2'].value:
                redirect('cadastro')

            name=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha'].value()

            print(name+email+senha)

            if User.objects.filter(username=name).exists():
                redirect('cadastro')

            usuario = User(username=name,
                           email=email,
                           password=senha)
            
            usuario.save()
            return redirect('login')


    return render(request, 'usuarios/cadastro.html', {'form': form})
   