from django.db import models

# Create your models here.

class Fotografia(models.Model):
    nome = models.CharField(max_length=10, null=False, blank=False)
    creditos = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    imagem = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"