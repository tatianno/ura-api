from django.contrib import admin
from .models import ProtocoloAtendimento


class ProtocoloAtendimentoModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'data',
        'numero',
        'cliente'
    ]


admin.site.register(ProtocoloAtendimento, ProtocoloAtendimentoModelAdmin)