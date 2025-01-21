from rest_framework.serializers import ModelSerializer, Serializer, CharField
from .models import Cliente


class ClienteModelSerializer(ModelSerializer):

    class Meta:
        model = Cliente
        fields = [
            'id',
            'nome',
            'em_massiva'
        ]


class ClienteDocumentoSerializer(Serializer):
    documento = CharField(max_length=50)