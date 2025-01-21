from rest_framework.serializers import ModelSerializer
from .models import ProtocoloAtendimento


class ProtocoloAtendimentoModelSerializer(ModelSerializer):

    class Meta:
        model = ProtocoloAtendimento
        fields = [
            'id',
            'data',
            'cliente',
            'telefone',
            'numero'
        ]
        