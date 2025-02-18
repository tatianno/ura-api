from agi.base_agi import BaseAgi
from .constants import LIMITE_TENTATIVAS
from entities.cliente import Cliente
from .exceptions import ExcedidoLimiteTentativasException
from services.base_service import BaseApiClienteService


class MenuCliente:

    def __init__(self, api_service: BaseApiClienteService, agi: BaseAgi):
        self._api_service = api_service
        self._agi = agi
    
    def _reproduzir_prompt_opcao_desejada(self) -> Cliente:
        opcao_desejada = None
        opcoes_validas = ['1', '2']
        tentativas = 0

        while not opcao_desejada and tentativas < LIMITE_TENTATIVAS:

            try:
                opcao_desejada = self._agi.reproduzir_prompt(audio='prompt_menu_cliente')

            
            finally:
                tentativas += 1
        
        raise ExcedidoLimiteTentativasException()