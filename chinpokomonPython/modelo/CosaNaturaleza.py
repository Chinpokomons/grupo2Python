from Naturaleza import Naturaleza

class CosaNaturaleza(Naturaleza):

    def __init__(self, nombre):
        Naturaleza.__init__ = nombre

    def tieneVentaja(self, naturaleza):
        return  True if naturaleza.getNombre() == "Robot"  else False