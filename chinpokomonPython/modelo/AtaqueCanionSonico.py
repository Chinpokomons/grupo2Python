from Ataque import Ataque

class AtaqueCanionSonico(Ataque):
    def __init__(self, valorDeAtaque,valorAtaqueNaturaleza):
        super().__init__(valorDeAtaque,valorAtaqueNaturaleza)

    def toString(self):
        return "Canion Sonico"