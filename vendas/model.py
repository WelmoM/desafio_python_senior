from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Venda:
    date: date
    produto: str
    qtdy: int
    preco: float

    @property
    def total(self) -> float:
        return self.qtdy * self.preco