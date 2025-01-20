from django.http import HttpResponseNotFound
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Cliente
from .serializers import ClienteModelSerializer, ClienteDocumentoSerializer
from boleto.serializers import BoletoModelSerializer


class ClienteModelViewSet(GenericViewSet):
    queryset = Cliente.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ClienteDocumentoSerializer
    serializer_class_boleto = BoletoModelSerializer
    serializer_class_cliente = ClienteModelSerializer

    @action(detail=True, methods=['GET'], url_path='consultar-boleto')
    def consultar_boleto(self, request, pk):
        cliente: Cliente = self.get_object()
        boletos = cliente.boleto_set.all()
        serializer = self.get_serializer(boletos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'], url_path='consultar-documento')
    def consultar_documento(self, request):
        queryset = self.get_queryset()
        serializer: ClienteDocumentoSerializer = self.get_serializer(request.data)
        documento = serializer.data.get('documento')

        if not queryset.filter(documento=documento).exists():
            return HttpResponseNotFound()

        cliente = queryset.get(documento=documento)
        serializer = self.serializer_class_cliente(
            cliente,
            context={'request': request, 'view': self}
        )
        return Response(serializer.data)
    
    def get_serializer_class(self):

        if self.action == 'consultar_boleto':
            return self.serializer_class_boleto

        elif self.action == 'consultar_documento':
            return self.serializer_class_documento
        
        return super().get_serializer_class()