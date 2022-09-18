from BuilerOfChinpokomon import BuilderOfChinpokomon
from Builder import Builder

class GeneradorDeChinpokomon:

    def __init__(self):
        self._builder = None

    #@property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def buildZapato(self):
        self._builder.setNombre("Zapato")
        self._builder.setVida(30)
        self._builder.setAtaques(["Ataque Zapato"])
        self._builder.setNaturaleza("Cosa")
        return self._builder.chinpokomon()

    def buildGallotronix(self):
        self._builder.setNombre("Gallotronix")
        self._builder.setVida(30)
        self._builder.setAtaques(["Ataque Zapato"])
        self._builder.setNaturaleza("Cosa")
        return self._builder.chinpokomon()

    def buildZapato(self):
        self._builder.setNombre("Zapato")
        self._builder.setVida(30)
        self._builder.setAtaques(["Ataque Zapato"])
        self._builder.setNaturaleza("Cosa")
        return self._builder.chinpokomon()