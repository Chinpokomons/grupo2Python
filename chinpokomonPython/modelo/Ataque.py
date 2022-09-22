import random
from Chinpokomon import Chinpokomon


class Ataque(object):
    def __init__(self, valorDeAtaque, valorAtaqueNaturaleza):
        self.valorDeAtaque = valorDeAtaque
        self.valorAtaqueNaturaleza = valorAtaqueNaturaleza
        self.random = random

    # getters
    @property
    def random(self):
        return self.random

    @property
    def valorDeAtaque(self):
        return self.valorDeAtaque

    @property
    def valorAtaqueNaturaleza(self):
        return self.valorAtaqueNaturaleza

    @valorAtaqueNaturaleza.setter
    def valorAtaqueNaturaleza(self, valorAtaqueNatural):
        self.valorAtaqueNaturaleza = valorAtaqueNatural

    def generarEfecto(self, chinpokomon1, chinpokomon2):
        if self.sePuedeAtacar(chinpokomon1, chinpokomon2):
            chinpokomon2.vida(chinpokomon2.vida() - self.valorDeAtaque -
                              self.danioExtraNaturaleza(chinpokomon1, chinpokomon2))

    def sePuedeAtacar(self, chinpokomon1, chinpokomon2):
        return chinpokomon2.vida() > 0 or chinpokomon1.vida() > 0

    # def valorDelAtaque(self):
    #     return self.valorDeAtaque

    # def getRandom(self):
    #     return self.__random

    # def setValorAtaqueNaturaleza(self, valorAtaqueNatural):
    #     self.__valorAtaqueNaturaleza=valorAtaqueNatural

    def generarRandom(self, valorMaximoExcluyente):
        return self.random().randint(0, valorMaximoExcluyente)

    def danioExtraNaturaleza(self, chinpokomon1, chinpokomon2):
        # //determinamos si el chinpokomon1 tiene ventaja de naturaleza sobre el chinpokomon2
        # // si tiene ventaja por naturaleza accedera a este if y aumentara el ataque instanciado al inicio + daño adicional

        if(chinpokomon1.naturaleza().tieneVentaja(chinpokomon2.naturaleza())):
            return self.valorAtaqueNaturaleza
        else:
            return 0
