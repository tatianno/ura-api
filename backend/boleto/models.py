from django.db import models
from cliente.models import Cliente

#34191790010104351004791020150008799190026000
class Boleto(models.Model):
    codigo_barras = models.CharField(max_length=50)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.codigo_barras
