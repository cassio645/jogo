from django.contrib import admin
from .models import Tema, Palavra

class TemaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}
    ordering = ('nome',)


class PalavraAdmin(admin.ModelAdmin):
    list_display = ("resposta", "tema", "wiki")
    list_filter=('tema', )


admin.site.register(Tema, TemaAdmin)
admin.site.register(Palavra, PalavraAdmin)