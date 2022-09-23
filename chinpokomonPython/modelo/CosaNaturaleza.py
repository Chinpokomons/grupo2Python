from Naturaleza import Naturaleza


class CosaNaturaleza(Naturaleza):

    def __init__(self, nombre):
        super().__init__(nombre)

    def tieneVentaja(self, naturaleza):
        return True if naturaleza.nombre == "Robot" else False
