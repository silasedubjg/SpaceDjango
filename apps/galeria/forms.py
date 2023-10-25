from django import forms

from apps.galeria.models import Fotografia


# class FotografiaForms(forms.ModelForm):
#     class Meta:
#         model = Fotografia,
#         exclude = ['publicada', ],



#         labels = {
#             'descricao': 'Descrição',
#             'data_fotografia': 'Data de registro',
#             'usuario': 'Usuário',
#         }


class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels = {
            'descricao':'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário',
        }       
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%d/%m/%Y'),
            'usuario': forms.Select(attrs={'class': 'form-control'}),

        }