from abc import ABC, abstractmethod


class BaseAgi(ABC):

    @abstractmethod
    def reproduzir_mensagem(self, audio: str): ...

    @abstractmethod
    def reproduzir_prompt(self, audio: str, timeout: int=3) -> str:...

    @abstractmethod
    def direcionar_chamada(self, destino: str): ...