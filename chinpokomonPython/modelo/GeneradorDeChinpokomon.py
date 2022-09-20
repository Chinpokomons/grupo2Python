from BuilderOfChinpokomon import BuilderOfChinpokomon
from Builder import Builder
from AtaqueCanionSonico import AtaqueCanionSonico
from AtaqueGarraMecanica import AtaqueGarraMecanica
from AtaquePomadaWassington import AtaquePomadaWassington
from AtaqueRayoVeloz import AtaqueRayoVeloz
from AtaqueZapatazo import AtaqueZapatazo
from Naturaleza import Naturaleza
from AnimalNaturaleza import AnimalNaturaleza
from RobotNaturaleza import RobotNaturaleza
from CosaNaturaleza import CosaNaturaleza
from CompuestoNaturalezas import CompuestoNaturalezas
from GeneracionDeRandom import NumAleatorio

random = NumAleatorio()


class GeneradorDeChinpokomon:

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def buildGallotronix(self):
        self._builder.setRandom(random)
        self._builder.setNombre("Gallotronix")
        self._builder.setVida(30)
        ataqueGarraMecanica = self.generarAtaqueAtaqueGarraMecanica()
        ataquesGallotronix = [ataqueGarraMecanica]
        self._builder.setAtaques(ataquesGallotronix)
        naturalezaRobot = self.generarNaturalezaRobot()
        self._builder.setNaturaleza(naturalezaRobot)
        return self._builder.chinpokomon()

    def buildZapato(self):
        self._builder.setRandom(random)
        self._builder.setNombre("Zapato")
        self._builder.setVida(30)
        ataqueZapato = self.generarAtaqueZapatazo()
        ataquesZapato = [ataqueZapato]
        self._builder.setAtaques(ataquesZapato)
        naturalezaCosa = self.generarNaturalezaCosa()
        self._builder.setNaturaleza(naturalezaCosa)
        return self._builder.chinpokomon()

    def buildZapatoEspecial(self):
        self._builder.setRandom(random)
        self._builder.setNombre("Zapato")
        self._builder.setVida(30)
        ataqueZapato = self.generarAtaqueZapatazo()
        ataquePomadaWassington = self.generarAtaqueAtaquePomadaWassington()
        ataquesZapato = [ataqueZapato, ataquePomadaWassington]
        self._builder.setAtaques(ataquesZapato)
        naturalezaCosa = self.generarNaturalezaCosa()
        self._builder.setNaturaleza(naturalezaCosa)
        return self._builder.chinpokomon()

    def buildCarnotron(self):
        self._builder.setRandom(random)
        self._builder.setNombre("Carnotron")
        self._builder.setVida(30)
        ataqueVeloz = self.generarAtaqueRayoVeloz()
        ataqueCanionSonico = self.generarAtaqueAtaqueCanionSonico()
        ataquesCarnotron = [ataqueVeloz, ataqueCanionSonico]
        self._builder.setAtaques(ataquesCarnotron)
        naturalezaAnimal = self.generarNaturaleza()
        self._builder.setNaturaleza(naturalezaAnimal)
        return self._builder.chinpokomon()

    def generarNaturaleza(self):
        return AnimalNaturaleza("Animal")

    def generarNaturalezaRobot(self):
        return RobotNaturaleza("Robot")

    def generarNaturalezaCosa(self):
        return CosaNaturaleza("Cosa")

    def generarNaturalezaCompuesto(self):
        return CompuestoNaturalezas()

    def generarAtaqueAtaqueCanionSonico(self):
        return AtaqueCanionSonico(4,1)

    def generarAtaqueAtaqueGarraMecanica(self):
        return AtaqueGarraMecanica(2,2)

    def generarAtaqueAtaquePomadaWassington(self):
        return AtaquePomadaWassington(5,1)

    def generarAtaqueRayoVeloz(self):
        return AtaqueRayoVeloz(3,1)

    def generarAtaqueZapatazo(self):
        return AtaqueZapatazo(1,3)
