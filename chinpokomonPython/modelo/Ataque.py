import random
from Chinpokomon import Chinpokomon
#import GeneracionDeRandom
class Ataque(object):
    def __init__(self, valorDeAtaque, valorAtaqueNaturaleza):
        self.__valorDeAtaque = valorDeAtaque
        self.__valorAtaqueNaturaleza = valorAtaqueNaturaleza
        self.__random = random
        #self.__random = GeneracionDeRandom.NumAleatorio()

    # getters
    @property
    def random(self):
        return self.__random

    @random.setter
    def random(self,nuevo):
      self.__random = nuevo
    
    @property
    def valorDeAtaque(self):
        return self.__valorDeAtaque

    @valorDeAtaque.setter
    def valorDeAtaque(self,nuevo):
         self.__valorDeAtaque = nuevo

    @property
    def valorAtaqueNaturaleza(self):
        return self.__valorAtaqueNaturaleza

    @valorAtaqueNaturaleza.setter
    def valorAtaqueNaturaleza(self, nuevo):
        self.__valorAtaqueNaturaleza = nuevo

    def generarEfecto(self, chinpokomon1, chinpokomon2):
        if self.sePuedeAtacar(chinpokomon1, chinpokomon2):
            chinpokomon2.vidaInChinpokomon = chinpokomon2.vidaInChinpokomon - self.valorDeAtaque - self.danioExtraNaturaleza(chinpokomon1, chinpokomon2)

    def sePuedeAtacar(self, chinpokomon1, chinpokomon2):
        return chinpokomon2.vidaInChinpokomon > 0 or chinpokomon1.vidaInChinpokomon > 0

    def generarRandom(self, valorMaximoExcluyente):
        return self.random.randint(0, valorMaximoExcluyente)

#    def generarRandom(self,valorMaximoExcluyente):
#      return self.random.generarRandom(valorMaximoExcluyente)    
    
    def danioExtraNaturaleza(self, chinpokomon1: Chinpokomon, chinpokomon2: Chinpokomon):
        # //determinamos si el chinpokomon1 tiene ventaja de naturaleza sobre el chinpokomon2
        # // si tiene ventaja por naturaleza accedera a este if y aumentara el ataque instanciado al inicio + daño adicional

        if(chinpokomon1.naturalezaInChinpokomon.tieneVentaja(chinpokomon2.naturalezaInChinpokomon)):
            return self.valorAtaqueNaturaleza
        else:
            return 0
