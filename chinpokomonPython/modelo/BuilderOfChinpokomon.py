from Builder import Builder
from Chinpokomon import Chinpokomon
class BuilderOfChinpokomon(Builder):

    def __init__(self):
        self.__chinpokomon = None
        self.reset()

    @property
    def chinpokomon(self):
      return self.__chinpokomon
    
    def reset(self):
        self.__chinpokomon = Chinpokomon()

    def resultado(self):
          chinpokomon = self.chinpokomon
          self.reset()
          return chinpokomon

    def setNombre(self, nombre):
        print(self.chinpokomon)
        self.chinpokomon.nombreInChinpokomon = nombre

    def setVida(self, vida):
        self.chinpokomon.vidaInChinpokomon = vida

    def setAtaques(self, listaDeAtaques):
        self.chinpokomon.listaAtaquesInChinpokomon = listaDeAtaques

    def setNaturaleza(self, naturaleza):
        self.chinpokomon.naturalezaInChinpokomon = naturaleza

    def setRandom(self, random):
        self.chinpokomon.randomInChinpokomon = random
