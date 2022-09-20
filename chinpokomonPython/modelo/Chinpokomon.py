class Chinpokomon():

    # aca irian los atributos, agregar property
    def __init__(self):
        self.__nombre = None
        self.__vida = None
        self.__listaAtaques = []
        self.__naturaleza = None
        self.__random = None

    def getRandom(self):
        return self.__random

    def setRandom(self, random):
        self.__random = random

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def getVida(self):
        return self.vida

    def setVida(self, vida):
        self.vida = vida

    def getAtaques(self):
        return self.listaAtaques

    def setAtaques(self, listaDeAtaques):
        self.listaAtaques = listaDeAtaques

    def setNaturaleza(self, naturaleza):
        self.naturaleza = naturaleza

    def ataque(self, unChimpokomon):
        if (self.noEstaMuertoOtroChimpokomon(unChimpokomon) and self.estoyVivo()):
            self.atacarSegunAtaqueSeleccionado(unChimpokomon)

    def atacarSegunAtaqueSeleccionado(self, chimpokomonAAtacar):
        if(len(self.getAtaques()) == 1):
            self.getAtaques()[0].generarEfecto(self, chimpokomonAAtacar)
        else:
            ataqueElegido = self.getrandom().generarRandom(len(self.getAtaques()))
            self.getAtaques()[ataqueElegido].generarEfecto(
                self, chimpokomonAAtacar)

    def estoyVivo(self):
        return self.getVida() > 0

    def noEstaMuertoOtroChimpokomon(self, chimpokomon):
        return chimpokomon.getVida() > 0
