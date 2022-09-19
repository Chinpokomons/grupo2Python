from InterfaceNaturaleza import Natural

class Naturaleza(Natural):

    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def tieneVentaja(self, naturaleza):
        return True
