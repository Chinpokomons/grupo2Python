import random


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


class NumAleatorio:

    def generarRandom(self, num):
        return random.randint(0, num-1)


class ChinpokomonPrueba():

    # aca irian los atributos, agregar property
    def __init__(self):
        self.nombre = None
        self.vida = None
        self.listaAtaques = []
        self.naturaleza = None
        self.random = None

    @property
    def random(self):
        return self.random

    @random.setter
    def random(self, random):
        self.random = random

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre

    @property
    def naturaleza(self):
        return self.naturaleza

    @naturaleza.setter
    def naturaleza(self, naturaleza):
        self.naturaleza = naturaleza

    @property
    def vida(self):
        return self.vida

    @vida.setter
    def vida(self, vida):
        self.vida = vida

    @property
    def listaAtaques(self):
        return self.listaAtaques

    @listaAtaques.setter
    def listaAtaques(self, listaDeAtaques):
        self.listaAtaques = listaDeAtaques

    def ataque(self, unChimpokomon):
        if (self.noEstaMuertoOtroChimpokomon(unChimpokomon) and self.estoyVivo()):
            self.atacarSegunAtaqueSeleccionado(unChimpokomon)

    def atacarSegunAtaqueSeleccionado(self, chimpokomonAAtacar):
        if(len(self.listaAtaques()) == 1):

            ataque = self.listaAtaques()[0]
            ataque.generarEfecto(self, chimpokomonAAtacar)
        else:
            cantidadDeAtaques = len(self.listaAtaques())
            rand = self.random()
            ataqueElegido = rand.generarRandom(cantidadDeAtaques)
            ataque = self.listaAtaques()[ataqueElegido]
            ataque.generarEfecto(self, chimpokomonAAtacar)

    def estoyVivo(self):
        return self.vida() > 0

    def noEstaMuertoOtroChimpokomon(self, chimpokomon):
        return chimpokomon.vida() > 0

    def toString(self):
        return self.nombre() + " " + str(self.vida())


chinpo1 = ChinpokomonPrueba()
print(chinpo1.nombre)
