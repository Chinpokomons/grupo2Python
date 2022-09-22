from Ataque import Ataque
from Chinpokomon import Chinpokomon


class AtaquePomadaWassington(Ataque):
    
    def __init__(self, valorDeAtaque, valorAtaqueNaturaleza):
        super().__init__(valorDeAtaque, valorAtaqueNaturaleza)

    def generarEfecto(self, chinpokomon1: Chinpokomon, chinpokomon2: Chinpokomon):
        nuevaVida = chinpokomon1.vidaInChinpokomon + self.valorDeAtaque
        chinpokomon1.vidaInChinpokomon = nuevaVida
