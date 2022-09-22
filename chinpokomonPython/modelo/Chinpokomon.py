class Chinpokomon(object):

    # aca irian los atributos, agregar property
    def __init__(self):
        self.__nombreInChinpokomon= None
        self.__vidaInChinpokomon = None
        self.__listaAtaquesInChinpokomon = []
        self.__naturalezaInChinpokomon = None
        self.__randomInChinpokomon = None

    @property
    def nombreInChinpokomon(self):
      return self.__nombreInChinpokomon
    
    @nombreInChinpokomon.setter #Propiedad SETTER
    def nombreInChinpokomon(self, nuevo):
        self.__nombreInChinpokomon = nuevo

    @property
    def vidaInChinpokomon(self):
      return self.__vidaInChinpokomon

    @vidaInChinpokomon.setter
    def vidaInChinpokomon(self,nuevo):
      self.__vidaInChinpokomon = nuevo
    
    @property
    def listaAtaquesInChinpokomon(self):
      return self.__listaAtaquesInChinpokomon

    @listaAtaquesInChinpokomon.setter
    def listaAtaquesInChinpokomon(self,nuevo):
      self.__listaAtaquesInChinpokomon = nuevo
    
    @property
    def naturalezaInChinpokomon(self):
      return self.__naturalezaInChinpokomon

    @naturalezaInChinpokomon.setter
    def naturalezaInChinpokomon(self,nuevo):
      self.__naturalezaInChinpokomon = nuevo

    @property
    def randomInChinpokomon(self):
      return self.__randomInChinpokomon

    @randomInChinpokomon.setter
    def randomInChinpokomon(self,nuevo):
      self.__randomInChinpokomon = nuevo
    
    def ataque(self, unChimpokomon):
      if (self.noEstaMuertoOtroChimpokomon(unChimpokomon) and self.estoyVivo()):
            self.atacarSegunAtaqueSeleccionado(unChimpokomon)

    def atacarSegunAtaqueSeleccionado(self, chimpokomonAAtacar):
        if(self.cantidadDeAtaques == 1):
            ataque = self.listaAtaquesInChinpokomon[0]
            ataque.generarEfecto(self, chimpokomonAAtacar)
        else:
            cantidadDeAtaques = len(self.listaAtaquesInChinpokomon)
            rand = self.randomInChinpokomon
            ataqueElegido = rand.generarRandom(cantidadDeAtaques)
            ataque = self.listaAtaquesInChinpokomon[ataqueElegido]
            ataque.generarEfecto(self, chimpokomonAAtacar)

    def estoyVivo(self):
        return self.vidaInChinpokomon > 0

    def noEstaMuertoOtroChimpokomon(self, chimpokomon):
        return chimpokomon.vidaInChinpokomon > 0

    def tostring(self):
        return self.nombreInChinpokomon + " tiene de vida: " +  str(self.vidaInChinpokomon)

    def cantidadDeAtaques(self):
        return len(self.listaAtaques)
