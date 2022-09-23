from Ataque import Ataque
class AtaqueZapatazo(Ataque):
    
    def __init__(self, valorDeAtaque,valorAtaqueNaturaleza):
        super().__init__(valorDeAtaque,valorAtaqueNaturaleza)
        
    def generarEfecto(self,chinpokomon1, chinpokomon2,log):
        super().generarEfecto(chinpokomon1, chinpokomon2,log)
        if(self.random.generarRandom(2) == 1):
            log.warn("El ataque Zapatazo fue especial y ataco dos veces")
            super().generarEfecto(chinpokomon1, chinpokomon2,log)

    def toString(self):
        return "Zapatazo"
        