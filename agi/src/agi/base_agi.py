from abc import ABC, abstractmethod


class BaseAgi(ABC):

    @abstractmethod
    def reproduzir_mensagem(self): ...

    @abstractmethod
    def direcionar_chamada(self): ...