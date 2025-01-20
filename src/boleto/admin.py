from django.contrib import admin
from .models import Boleto


class BoletoModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'codigo_barras',
        'cliente'
    ]


admin.site.register(Boleto, BoletoModelAdmin)