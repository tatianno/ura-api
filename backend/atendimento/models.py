from django.db import models
from django.dispatch import receiver
from cliente.models import Cliente


class ProtocoloAtendimento(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )
    telefone = models.CharField(max_length=20, null=True, blank=True)
    _numero = models.PositiveIntegerField(null=True, blank=True)

    @property
    def numero(self):
        return f'{self.data.strftime("%Y%m%d")}{self._numero}'

    def __str__(self) -> str:
        return self.numero


@receiver(models.signals.pre_save, sender=ProtocoloAtendimento)
def executar_acoes_apos_salvar(sender, instance, **kwargs):

    if not instance._numero:
        if sender.objects.all().exists():
            ultimo_protocolo = sender.objects.last()
            instance._numero = ultimo_protocolo._numero + 1

        else:
            instance._numero = 1