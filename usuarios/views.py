from django.shortcuts import render, redirect

from django.http import HttpResponse

from templates import *

from usuarios.forms import LoginForm, cadastroForm

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages
# Create your views here.

def login(request):
    form= LoginForm()

    if request.method=='POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

            print(nome+senha)
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )

            if usuario is not None:
                print('não é none')
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso")
                return redirect('Home')
            else:
                messages.error(request, "erro ao logar")
                return redirect('login')
    
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = cadastroForm()

    if request.method == 'POST':
        form = cadastroForm(request.POST)
        name=form['nome_cadastro'].value()
        if User.objects.filter(username=name):
            messages.success(request, f"Usuário {name} já cadastrado")
            return render(request, 'usuarios/cadastro.html', {'form': form})
        if form.is_valid:
            if form['senha'].value != form['senha2'].value:
                redirect('cadastro')

            name=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha'].value()

            if User.objects.filter(username=name).exists():
                messages.success(request, f"Usuário {name} já cadastrado")
                redirect('cadastro')

            usuario = User(username=name,
                           email=email,
                           password=senha)
            
            usuario.save()
            messages.success(request, f"{name} logado com sucesso")
            return redirect('login')
        else:
            
            return render(request, 'usuarios/cadastro.html', {'form': form})


    return render(request, 'usuarios/cadastro.html', {'form': form})
   
def logout(request):
    auth.logout(request)
    messages.success(request, "logout realizado com sucesso")
    return redirect('login')

