from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import mixins, GenericViewSet
from .models import ProtocoloAtendimento
from .serializers import ProtocoloAtendimentoModelSerializer


class ProtocoloAtendimentoModelViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = ProtocoloAtendimento.objects.all()
    serializer_class = ProtocoloAtendimentoModelSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        '''
        Criar protocolo de atendimento

        Endpoint permite criação de protocolos de atendimento.
        '''
        return super().create(request, *args, **kwargs)