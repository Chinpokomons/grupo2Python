from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def chinpokomon(self):
        pass

    @abstractmethod
    def setNombre(self, nombre):
        pass

    @abstractmethod
    def setAtaques(self, listaDeAtaques):
        pass

    @abstractmethod
    def setVida(self, vida):
        pass

    @abstractmethod
    def setNaturaleza(self, naturaleza):
        pass

    @abstractmethod
    def setRandom(self, random):
        pass
