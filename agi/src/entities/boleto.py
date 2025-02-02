from dataclasses import dataclass


@dataclass
class Boleto:
    id: int
    codigo_barras: bool