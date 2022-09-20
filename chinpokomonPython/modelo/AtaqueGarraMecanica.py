from Ataque import Ataque
from Chinpokomon import Chinpokomon
class AtaqueGarraMecanica(Ataque):
    def __init__(self, valorDeAtaque,valorAtaqueNaturaleza):
        super().__init__(valorDeAtaque,valorAtaqueNaturaleza)
        

    def generarEfecto(self, chinpokomon1, chinpokomon2):
        random = self.generarRandom(10)
        if(random == 1):
            self.sacarMitadDeLaVidaQueLeQueda(chinpokomon2)
        else:
            self.generarEfectoBasico(chinpokomon1, chinpokomon2)

    def obtenerVidaRestanteDeChinpokomon(self, chinpokomon : Chinpokomon):
        return chinpokomon.getVida()

    def sacarMitadDeLaVidaQueLeQueda(self, chinpokomon):
        chinpokomon.setVida(self.obtenerVidaRestanteDeChinpokomon(
            chinpokomon) - self.obtenerVidaRestanteDeChinpokomon(chinpokomon)/2)

    def generarEfectoBasico(self, chinpokomon1, chinpokomon2: Chinpokomon):
        if self.sePuedeAtacar(chinpokomon1, chinpokomon2):
            chinpokomon2.setVida(chinpokomon2.getVida() - self.valorDeAtaque -
                              self.danioExtraNaturaleza(chinpokomon1, chinpokomon2))
