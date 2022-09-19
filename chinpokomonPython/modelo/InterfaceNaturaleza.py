from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class InterfaceNaturaleza(ABC):
    """
    Interfaz con metodos abstractos de naturaleza
    """
    @abstractmethod
    def getNombre(self):
        pass

    @abstractmethod
    def tieneVentaja(self, chinpokomon):
        pass