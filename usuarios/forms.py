from django import forms

class LoginForm(forms.Form):
    nome_login=forms.CharField(
        max_length=100,
        label="usuario",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ex: Silas E.', 'class': 'form-control'},
    )
        
    )
    senha=forms.CharField(
        max_length=100,
        label="Senha",
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'}),

    )