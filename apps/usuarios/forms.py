from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    nome_login = forms.CharField(
        max_length=100,
        label="usuario",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ex: Silas E.', 'class': 'form-control'},
                               )

    )
    senha = forms.CharField(
        max_length=100,
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'}),

    )


class cadastroForm(forms.Form):
    nome_cadastro= forms.CharField(
        max_length=100,
        label="usuario",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ex: Silas E.', 'class': 'form-control'},
                               )

    )
    email = forms.EmailField(
        max_length=100,
        label="Senha",
        required=True,
        widget=forms.EmailInput(
            attrs={'placeholder': 'Ex: usuario@mysite.com', 'class': 'form-control'}),

    )
    senha = forms.CharField(
        max_length=100,
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'}),

    )
    senha2 = forms.CharField(
        max_length=100,
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'}),

    )

    def clean_nome_cadastro(self, *args, **kwargs):
        nome = self.cleaned_data.get('nome_cadastro')
        print(nome)
        if nome:
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                usuario = User.objects.all().filter(username=nome)
                if nome == usuario['username']:
                    raise forms.ValidationError('usuario ja existe')
                else:
                    return nome

   
