from rest_framework.serializers import ModelSerializer
from .models import Boleto


class BoletoModelSerializer(ModelSerializer):

    class Meta:
        model = Boleto
        fields = [
            'id',
            'codigo_barras'
        ]