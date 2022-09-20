import random
from Chinpokomon import Chinpokomon
class Ataque(object):
    def __init__(self, valorDeAtaque,valorAtaqueNaturaleza):
        self.__valorDeAtaque = valorDeAtaque
        self.__valorAtaqueNaturaleza = valorAtaqueNaturaleza
        self.__random = random

    def generarEfecto(self, chinpokomon1, chinpokomon2):
        if self.sePuedeAtacar(chinpokomon1, chinpokomon2):
            chinpokomon2.setVida(chinpokomon2.getVida() - self.valorDeAtaque - \
                              self.danioExtraNaturaleza(chinpokomon1, chinpokomon2))

    def sePuedeAtacar(self, chinpokomon1, chinpokomon2):
        return chinpokomon2.getVida() > 0 or chinpokomon1.getVida() > 0

    # getters
    @ property
    def random(self):
        return self.__random

    @ property
    def valorDeAtaque(self):
        return self.__valorDeAtaque

    @ property
    def valorAtaqueNaturaleza(self):
        return self.__valorAtaqueNaturaleza

    def valorDelAtaque(self):
        return self.valorDeAtaque
    
    def getRandom(self):
        return self.__random

    def setValorAtaqueNaturaleza(self, valorAtaqueNatural):
        self.__valorAtaqueNaturaleza=valorAtaqueNatural

    def generarRandom(self, valorMaximoExcluyente):
        return self.getRandom().randint(0, valorMaximoExcluyente)

    def danioExtraNaturaleza(self,chinpokomon1: Chinpokomon, chinpokomon2: Chinpokomon):
        # //determinamos si el chinpokomon1 tiene ventaja de naturaleza sobre el chinpokomon2
        # // si tiene ventaja por naturaleza accedera a este if y aumentara el ataque instanciado al inicio + daño adicional
       
        if(chinpokomon1.getNaturaleza().tieneVentaja(chinpokomon2.getNaturaleza())):
            return self.valorAtaqueNaturaleza
        else:
            return 0
