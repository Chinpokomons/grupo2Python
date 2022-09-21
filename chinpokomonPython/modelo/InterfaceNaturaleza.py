from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class InterfaceNaturaleza(ABC):
    """
    Interfaz que representa una naturaleza.
  """
    @property
    def nombre(self):
        pass

    def tieneVentaja(self, chinpokomon):
        pass
