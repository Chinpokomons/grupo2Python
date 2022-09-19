from random import Random


class Ataque:
    def __init__(self, valorDeAtaque):
        self.__valorDeAtaque = valorDeAtaque
        self.__valorAtaqueNaturaleza = 0
        self.__random = Random.random()

    def generarEfecto(self, Chinpokomon chinpokomon1, Chinpokomon chinpokomon2):
        if self.sePuedeAtacar(chinpokomon1, chinpokomon2)):
            chinpokomon2.vida(chinpokomon2.vida - self.valorDeAtaque - \
                              self.danioExtraNaturaleza(chinpokomon1, chinpokomon2))

    def sePuedeAtacar(self, Chinpokomon chinpokomon1, Chinpokomon chinpokomon2):
        return chinpokomon2.vida() > 0 | chinpokomon1.vida() > 0

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

    @ valorAtaqueNaturaleza.setter
    def valorAtaqueNaturaleza(self, valorAtaqueNatural):
        self.__valorAtaqueNaturaleza=valorAtaqueNatural

    def generarRandom(self, valorMaximoExcluyente):
        return self.__random.randint(0, valorMaximoExcluyente)

    def danioExtraNaturaleza(self, Chinpokomon chinpokomon1, Chinpokomon chinpokomon2):
        # //determinamos si el chinpokomon1 tiene ventaja de naturaleza sobre el chinpokomon2
        # // si tiene ventaja por naturaleza accedera a este if y aumentara el ataque instanciado al inicio + daño adicional
        if(chinpokomon1.getNaturaleza().tieneVentaja(chinpokomon2.getNaturaleza())):
            return self.valorAtaqueNaturaleza
        else:
            return 0
