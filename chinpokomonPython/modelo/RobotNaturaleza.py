from Naturaleza import Naturaleza

class RobotNaturaleza(Naturaleza):

    def __init__(self, nombre):
        super().__init__(nombre)

    def tieneVentaja(self, naturaleza):
        return  True if naturaleza.getNombre() == "Animal"  else False