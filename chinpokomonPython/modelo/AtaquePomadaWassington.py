from modelo.Ataque import Ataque


def AtaquePomadaWassington(Ataque):

    def AtaquePomadaWassington(self, valorDeAtaque):
        super().super_method(valorDeAtaque)
    #   //agregamos el danio extra que realiza este ataque si tiene ventaja de naturaleza
    #     this.setValorAtaqueNaturaleza(1);

    def generarEfecto(self, Chinpokomon chinpokomon1, Chinpokomon chinpokomon2):
        print("Entre a pomada")
        chinpokomon1.vida(chinpokomon1.vida() + self.valorDeAtaque())
