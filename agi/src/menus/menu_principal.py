from validate_docbr import CPF, CNPJ
from agi.base_agi import BaseAgi
from entities.cliente import Cliente
from services.base_service import BaseApiClienteService


LIMITE_TENTATIVAS = 3

class DocumentoInvalidoException(Exception): ...


class ExcedidoLimiteTentativasException(Exception): ...


class MenuPrincipal:

    def __init__(self, api_service: BaseApiClienteService, agi: BaseAgi):
        self._api_service = api_service
        self._agi = agi
    
    def _reproduzir_prompt_informe_documento(self) -> Cliente:
        documento = None
        tentativas = 0

        while not documento and tentativas < LIMITE_TENTATIVAS:

            try:
                documento = self._agi.reproduzir_prompt(audio='prompt_documento')
                self._verificar_validade_documento(documento)
                cliente = self._api_service.consultar_cliente(documento)
                return cliente
            
            except DocumentoInvalidoException:
                documento = None
            
            finally:
                tentativas += 1
        
        raise ExcedidoLimiteTentativasException()
        
    def _verificar_validade_documento(self, documento: str) -> None:
        cpf = CPF()
        cnpj = CNPJ()

        if not cpf.validate(documento) and not cnpj.validate(documento):
            raise DocumentoInvalidoException()
            

    