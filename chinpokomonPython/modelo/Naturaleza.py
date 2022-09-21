from InterfaceNaturaleza import InterfaceNaturaleza


class Naturaleza(InterfaceNaturaleza):

    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    def tieneVentaja(self, naturaleza):
        return True
