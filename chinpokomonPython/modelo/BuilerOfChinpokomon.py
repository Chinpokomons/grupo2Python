from Builder import Builder
from Chinpokomon import Chinpokomon

class BuilderOfChinpokomon(Builder):

    def __init__(self):
        self._chinpokomon = Chinpokomon()

    def reset(self):
        self._chinpokomon = Chinpokomon()

    def chinpokomon(self):
        chinpokomon = self._chinpokomon
        self.reset()
        return chinpokomon

    def setNombre(self,nombre):
        self._chinpokomon.setNombre(nombre)

    def setVida(self,vida):
        self._chinpokomon.setVida(vida)

    def setAtaques(self,listaDeAtaques):
        self._chinpokomon.setAtaques(listaDeAtaques)

    def setNaturaleza(self,naturaleza):
        self._chinpokomon.setNaturaleza(naturaleza)