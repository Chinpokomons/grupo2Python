class Chinpokomon(object):

    # aca irian los atributos, agregar property
    def __init__(self):
        self.__nombre= None
        self.__vida = None
        self.__listaAtaques = []
        self.__naturaleza = None
        self.__random = None

    @property
    def nombre(self):
      return self.__nombre
    
    @nombre.setter #Propiedad SETTER
    def nombre(self, nuevo):
        self.__nombre = nuevo

    @property
    def vida(self):
      return self.__vida

    @vida.setter
    def vida(self,nuevo):
      self.__vida = nuevo
    
    @property
    def listaAtaques(self):
      return self.__listaAtaques

    @listaAtaques.setter
    def listaAtaques(self,nuevo):
      self.__listaAtaques = nuevo
    
    @property
    def naturaleza(self):
      return self.__naturaleza

    @naturaleza.setter
    def naturaleza(self,nuevo):
      self.__naturaleza = nuevo

    @property
    def random(self):
      return self.__random

    @random.setter
    def random(self,nuevo):
      self.random = nuevo
    
    def ataque(self, unChimpokomon):
      if (self.noEstaMuertoOtroChimpokomon(unChimpokomon) and self.estoyVivo()):
            self.atacarSegunAtaqueSeleccionado(unChimpokomon)

    def atacarSegunAtaqueSeleccionado(self, chimpokomonAAtacar):
        if(self.cantidadDeAtaques == 1):
            ataque = self.listaAtaques()[0]
            ataque.generarEfecto(self, chimpokomonAAtacar)
        else:
            cantidadDeAtaques = len(self.listaAtaques())
            rand = self.random
            ataqueElegido = rand.generarRandom(cantidadDeAtaques)
            ataque = self.listaAtaques()[ataqueElegido]
            ataque.generarEfecto(self, chimpokomonAAtacar)

    def estoyVivo(self):
        return self.vida > 0

    def noEstaMuertoOtroChimpokomon(self, chimpokomon):
        return chimpokomon.vida() > 0

    def tostring(self):
        return self.nombre + " tiene de vida: " +  str(self.vida)

    def cantidadDeAtaques(self):
        return len(self.listaAtaques)
