from InterfaceNaturaleza import InterfaceNaturaleza


class Naturaleza(InterfaceNaturaleza):

    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nuevo):
      self.__nombre = nuevo

    def tieneVentaja(self, naturaleza):
        return True
