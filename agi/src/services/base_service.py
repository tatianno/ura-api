from abc import ABC, abstractmethod
from entities.boleto import Boleto
from entities.cliente import Cliente
from entities.protocolo import Protocolo


class BaseApiClienteService(ABC):

    @abstractmethod
    def consultar_cliente(self, documento: str) -> Cliente: ...

    @abstractmethod
    def consultar_boletos(self, cliente_id: int) -> Boleto: ...

    @abstractmethod
    def gerar_protocolo_atendimento(self, cliente_id: int, telefone: str) -> Protocolo: ...