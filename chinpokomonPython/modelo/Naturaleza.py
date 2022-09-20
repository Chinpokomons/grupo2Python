from InterfaceNaturaleza import InterfaceNaturaleza


class Naturaleza(InterfaceNaturaleza):

    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def tieneVentaja(self, naturaleza):
        return True
