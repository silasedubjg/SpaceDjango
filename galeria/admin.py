from django.contrib import admin

# Register your models here.

from galeria.models import *

class ListaFotografias(admin.ModelAdmin):
    list_display = ("id","nome", "creditos")
    list_display_links = ("id","nome", "creditos")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 10

admin.site.register(Fotografia, ListaFotografias)