from Naturaleza import Naturaleza
from InterfaceNaturaleza import InterfaceNaturaleza
from typing import List


class CompuestoNaturalezas(Naturaleza):

    def __init__(self):
        super().__init__("Naturalezas")
        self.naturalezas: List[InterfaceNaturaleza] = []

    def agregar(self, naturaleza):
        self.naturalezas.append(naturaleza)

    def quitar(self, naturaleza):
        self.naturalezas.remove(naturaleza)

    def nombre(self):
        texto = self.naturalezas[0].nombre()

        for i in range(len(self.naturalezas)):
            if i != 0:
                texto = texto + " | " + self.naturalezas[i].nombre()

        return texto

    def tieneVentaja(self, naturaleza):
        valor = False

        for i in range(len(self.naturalezas)):
            if (self.naturalezas[i].tieneVentaja()):
                valor = True
                break

        return valor
