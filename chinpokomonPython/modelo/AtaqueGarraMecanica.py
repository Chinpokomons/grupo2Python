from Ataque import Ataque


def AtaqueGarraMecanica(Ataque):
    def AtaqueGarraMecanica(self, valorDeAtaque):
        super(valorDeAtaque)
        # //agregamos el danio extra que realiza este ataque si tiene ventaja de naturaleza
        # this.setValorAtaqueNaturaleza(2);

    def generarEfecto(self, chinpokomon1, chinpokomon2):
        random = self.generarRandom(10)
        if(random == 1):
            self.sacarMitadDeLaVidaQueLeQueda(chinpokomon2)
        else:
            self.generarEfectoBasico(chinpokomon1, chinpokomon2)

    def obtenerVidaRestanteDeChinpokomon(self, chinpokomon):
        return chinpokomon.vida()

    def sacarMitadDeLaVidaQueLeQueda(self, chinpokomon):
        chinpokomon.vida(self.obtenerVidaRestanteDeChinpokomon(
            chinpokomon) - self.obtenerVidaRestanteDeChinpokomon(chinpokomon)/2)

    def generarEfectoBasico(self, chinpokomon1, chinpokomon2):
        if self.sePuedeAtacar(chinpokomon1, chinpokomon2):
            chinpokomon2.vida(chinpokomon2.vida - self.valorDeAtaque -
                              self.danioExtraNaturaleza(chinpokomon1, chinpokomon2))
