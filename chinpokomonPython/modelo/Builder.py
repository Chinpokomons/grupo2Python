from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    def chinpokomon(self):
        pass

    def setNombre(self, nombre):
        pass
    
    def setAtaques(self, listaDeAtaques):
        pass
   
    def setVida(self, vida):
        pass

    def setNaturaleza(self, naturaleza):
        pass

    def setRandom(self, random):
        pass
