from django.db import models
from datetime import datetime
# Create your models here.

class Fotografia(models.Model):

    OPCOES_CATEGORIA = {
        ("NEBULOSA", "nebulosa"),
        ("GALAXIA", "galáxia")
    }
    nome = models.CharField(max_length=100, null=False, blank=False)
    creditos = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=150,choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    imagem = models.CharField(max_length=150, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"