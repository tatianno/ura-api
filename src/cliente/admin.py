from django.contrib import admin
from .models import Cliente


class ClienteModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'documento',
        'em_massiva'
    ]


admin.site.register(Cliente, ClienteModelAdmin)

