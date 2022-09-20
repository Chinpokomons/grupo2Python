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

    def buildZapato(self):
        ataqueZapato = self.generarAtaqueZapatazo()
        ataques = [ataqueZapato]
        naturalezaCosa = self.generarNaturalezaCosa()
        listaNaturalezas = self.generarNaturalezaCompuesto()
        listaNaturalezas.agregar(naturalezaCosa)
        self._builder.setRandom(random)
        self._builder.setNombre("Zapato")
        self._builder.setVida(30)
        self._builder.setAtaques(ataques)
        self._builder.setNaturaleza(listaNaturalezas)
        return self._builder.chinpokomon()

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
        ataquePomadaWassington = self.generarAtaqueAtaquePomadaWassington()
        ataquesZapato = [ataquePomadaWassington]
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

    def generarNaturaleza(self):
        return AnimalNaturaleza()

    def generarNaturalezaRobot(self):
        return RobotNaturaleza()

    def generarNaturalezaCosa(self):
        return CosaNaturaleza()

    def generarNaturalezaCompuesto(self):
        return CompuestoNaturalezas()

    def generarAtaqueAtaqueCanionSonico(self):
        return AtaqueCanionSonico()

    def generarAtaqueAtaqueGarraMecanica(self):
        return AtaqueGarraMecanica()

    def generarAtaqueAtaquePomadaWassington(self):
        return AtaquePomadaWassington()

    def generarAtaqueRayoVeloz(self):
        return AtaqueRayoVeloz()

    def generarAtaqueZapatazo(self):
        return AtaqueZapatazo()
