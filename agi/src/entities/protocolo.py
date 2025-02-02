from dataclasses import dataclass


@dataclass
class Protocolo:
    id: int
    data: str
    cliente: int
    telefone: str
    numero: str
