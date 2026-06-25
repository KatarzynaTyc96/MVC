from django.contrib import admin
from .models import Ksiazka


@admin.register(Ksiazka)
class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'autor', 'rok_wydania', 'data_dodania')
    search_fields = ('tytul', 'autor')
    list_filter = ('autor', 'rok_wydania')
