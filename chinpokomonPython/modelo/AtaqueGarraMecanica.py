from Ataque import Ataque
from Chinpokomon import Chinpokomon

class AtaqueGarraMecanica(Ataque):
    def __init__(self, valorDeAtaque, valorAtaqueNaturaleza):
        super().__init__(valorDeAtaque, valorAtaqueNaturaleza)

    def generarEfecto(self, chinpokomon1, chinpokomon2,log):
        random = self.generarRandom(10)
        if(random == 1):
            self.sacarMitadDeLaVidaQueLeQueda(chinpokomon2,log)
        else:
            self.generarEfectoBasico(chinpokomon1, chinpokomon2,log)

    def sacarMitadDeLaVidaQueLeQueda(self, chinpokomon: Chinpokomon,log):
        log.warn("El ataque Garra Mecanica fue especial y le saco la mitad de la vida que le quedaba al chinpokomon")
        chinpokomon.vidaInChinpokomon = self.obtenerVidaRestanteDeChinpokomon(
            chinpokomon) - self.obtenerVidaRestanteDeChinpokomon(chinpokomon)/2
    
    def obtenerVidaRestanteDeChinpokomon(self, chinpokomon: Chinpokomon):
        return chinpokomon.vidaInChinpokomon

    
    ##en python no se puede sobrecargar metodos, por lo que se crea un metodo que recibe un parametro mas
    def generarEfectoBasico(self, chinpokomon1, chinpokomon2: Chinpokomon,log):
        if self.sePuedeAtacar(chinpokomon1, chinpokomon2):
            log.warn("El ataque hizo de danio: " + str(self.valorDeAtaque + self.danioExtraNaturaleza(chinpokomon1, chinpokomon2)))
            chinpokomon2.vidaInChinpokomon = chinpokomon2.vidaInChinpokomon - self.valorDeAtaque - self.danioExtraNaturaleza(chinpokomon1, chinpokomon2)
        
    def toString(self):
        return "Garra Mecanica"