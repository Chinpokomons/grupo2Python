from Builder import Builder
from Chinpokomon import Chinpokomon


class BuilderOfChinpokomon(Builder):

    def __init__(self):
        self.chinpokomon = Chinpokomon()

    def reset(self):
        self.chinpokomon = Chinpokomon()

    @property
    def chinpokomon(self):
        chinpokomon = self.chinpokomon
        self.reset()
        return chinpokomon

    def setNombre(self, nombre):
        self.chinpokomon.nombre(nombre)

    def setVida(self, vida):
        self.chinpokomon.vida(vida)

    def setAtaques(self, listaDeAtaques):
        self.chinpokomon.listaAtaques(listaDeAtaques)

    def setNaturaleza(self, naturaleza):
        self.chinpokomon.naturaleza(naturaleza)

    def setRandom(self, random):
        self.chinpokomon.random(random)
