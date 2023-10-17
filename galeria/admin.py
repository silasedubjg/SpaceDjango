from django.contrib import admin

# Register your models here.

from galeria.models import *

class ListaFotografias(admin.ModelAdmin):
    list_display = ("id","nome", "creditos")
    list_display_links = ("id","nome", "creditos")
    search_fields = ("nome",)

admin.site.register(Fotografia, ListaFotografias)