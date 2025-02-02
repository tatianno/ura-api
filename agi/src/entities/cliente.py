from dataclasses import dataclass

@dataclass
class Cliente:
    id: int
    nome: str
    em_massiva: bool