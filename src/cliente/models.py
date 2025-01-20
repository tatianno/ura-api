from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=300)
    documento = models.CharField(max_length=50, unique=True)
    em_massiva = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome