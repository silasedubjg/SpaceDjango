from django import forms

class LoginForm(forms.Form):
    nome_login=forms.CharField(
        max_length=100,
        label="usuario",
        required=True
    )
    senha=forms.CharField(
        max_length=100,
        label="Senha",
        required=True,
        widget=forms.PasswordInput()

    )