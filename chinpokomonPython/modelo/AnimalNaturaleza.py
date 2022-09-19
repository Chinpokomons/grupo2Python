from Naturaleza import Naturaleza

class AnimalNaturaleza(Naturaleza):

    def __init__(self, nombre):
        Naturaleza.__init__ = nombre

    def tieneVentaja(self, naturaleza):
        return  True if naturaleza.getNombre() == "cosa"  else False