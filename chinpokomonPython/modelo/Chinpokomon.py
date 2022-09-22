from random import random


class Chinpokomon():

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
