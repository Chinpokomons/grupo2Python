from Ataque import Ataque
import GeneracionDeRandom
class AtaqueZapatazo(Ataque):

    def __init__(self, valorDeAtaque,valorAtaqueNaturaleza):
        super().__init__(valorDeAtaque,valorAtaqueNaturaleza)
        self.rand = GeneracionDeRandom.NumAleatorio()
        

    def generarEfecto(self,chinpokomon1, chinpokomon2):
        
        super().generarEfecto(chinpokomon1, chinpokomon2)
        if(self.rand.generarRandom(2) == 1):
            super().generarEfecto(chinpokomon1, chinpokomon2)
