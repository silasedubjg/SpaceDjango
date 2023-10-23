from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import User

class Fotografia(models.Model):

    OPCOES_CATEGORIA = {
        ("NEBULOSA", "nebulosa"),
        ("GALAXIA", "galáxia")
    }
    nome = models.CharField(max_length=100, null=False, blank=False)
    creditos = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=150,choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    imagem = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"