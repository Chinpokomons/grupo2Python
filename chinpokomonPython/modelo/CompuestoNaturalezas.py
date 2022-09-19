from Naturaleza import Naturaleza
from InterfaceNaturaleza import Natural
from typing import List

class CompuestoNaturalezas(Naturaleza):

    def __init__(self):
        Naturaleza.__init__("Naturalezas")
        self.naturalezas: List[Natural] = []

    def agregar(self, naturaleza):
        self.naturalezas.append(naturaleza)

    def quitar(self, naturaleza):
        self.naturalezas.remove(naturaleza)

    def getNombre(self):
        texto = self.naturalezas[0].getNombre()

        for i in range( len(self.naturalezas) ):
            if i != 0:
                texto = texto + " | " + self.naturalezas[i].getNombre()
        
        return texto

    
    def tieneVentaja(self, naturaleza):
        valor = False

        for i in range( len(self.naturalezas) ):
            if ( self.naturalezas[i].tieneVentaja() ):
                valor = True
                break

        return valor