from modelo.Ataque import Ataque


def AtaqueGarraMecanica(Ataque):
    def AtaqueGarraMecanica(self, valorDeAtaque):
        super().super_method(valorDeAtaque)
        # //agregamos el danio extra que realiza este ataque si tiene ventaja de naturaleza
        # this.setValorAtaqueNaturaleza(2);

    def generarEfecto(self, Chinpokomon chinpokomon1, Chinpokomon chinpokomon2):
        random = self.generarRandom(10)
        if(random == 1):
            print("ENTRE ACA")
            self.sacarMitadDeLaVidaQueLeQueda(chinpokomon2)
        else:
            super().super_method().generarEfecto(chinpokomon1, chinpokomon2)

    def obtenerVidaRestanteDeChinpokomon(self, Chinpokomon chinpokomon):
        return chinpokomon.vida()

    def sacarMitadDeLaVidaQueLeQueda(self, Chinpokomon chinpokomon):
        chinpokomon.vida(self.obtenerVidaRestanteDeChinpokomon(
            chinpokomon) - self.obtenerVidaRestanteDeChinpokomon(chinpokomon)/2)
