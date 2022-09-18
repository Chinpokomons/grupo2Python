class Chinpokomon():

    #aca irian los atributos, agregar property
    def __init__(self):
        self.nombre = None
        self.vida = None
        self.listaAtaques = []
        self.naturaleza = None

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setVida(self,vida):
        self.vida = vida

    def setAtaques(self,listaDeAtaques):
        self.ataques = listaDeAtaques

    def setNaturaleza(self,naturaleza):
        self.naturaleza = naturaleza