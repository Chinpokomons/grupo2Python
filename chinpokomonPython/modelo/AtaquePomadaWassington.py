from Ataque import Ataque

class AtaquePomadaWassington(Ataque):

    def __init__(self, valorDeAtaque,valorAtaqueNaturaleza):
       super().__init__(valorDeAtaque,valorAtaqueNaturaleza)
  
    def generarEfecto(self, chinpokomon1, chinpokomon2):
        
        nuevaVida = chinpokomon1.getVida() + self.valorDelAtaque()
        chinpokomon1.setVida(nuevaVida)
