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

class GeneradorDeChinpokomon:
    
    def __init__(self,builder):
        self.__builder = builder
        self.__random = NumAleatorio()
    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder):
        self.__builder = builder
    
    @property
    def random(self):
        return self.__random

    def buildGallotronix(self):
        self.builder.setRandom(self.random)
        self.builder.setNombre("Gallotronix")
        self.builder.setVida(25)
        ataqueGarraMecanica = self.generarAtaqueAtaqueGarraMecanica()
        ataquesGallotronix = [ataqueGarraMecanica]
        self.builder.setAtaques(ataquesGallotronix)
        naturalezaRobot = self.generarNaturalezaRobot()
        self.builder.setNaturaleza(naturalezaRobot)
        print(self.builder)
        return self.builder.resultado()

    def buildZapato(self):
        self.builder.setRandom(self.random)
        self.builder.setNombre("Zapato")
        self.builder.setVida(30)
        ataqueZapato = self.generarAtaqueZapatazo()
        ataquesZapato = [ataqueZapato]
        self.builder.setAtaques(ataquesZapato)
        naturalezaCosa = self.generarNaturalezaCosa()
        self.builder.setNaturaleza(naturalezaCosa)
        return self.builder.resultado()

    def buildZapatoEspecial(self):
        self.builder.setRandom(self.random)
        self.builder.setNombre("Zapato")
        self.builder.setVida(30)
        ataqueZapato = self.generarAtaqueZapatazo()
        ataquePomadaWassington = self.generarAtaqueAtaquePomadaWassington()
        ataquesZapato = [ataqueZapato, ataquePomadaWassington]
        self.builder.setAtaques(ataquesZapato)
        naturalezaCosa = self.generarNaturalezaCosa()
        self.builder.setNaturaleza(naturalezaCosa)
        return self.builder.resultado()

    def buildCarnotron(self):
        self.builder.setRandom(self.random)
        self.builder.setNombre("Carnotron")
        self.builder.setVida(20)
        ataqueVeloz = self.generarAtaqueRayoVeloz()
        ataqueCanionSonico = self.generarAtaqueAtaqueCanionSonico()
        ataquesCarnotron = [ataqueVeloz, ataqueCanionSonico]
        self.builder.setAtaques(ataquesCarnotron)
        naturalezaAnimal = self.generarNaturaleza()
        self.builder.setNaturaleza(naturalezaAnimal)
        return self.builder.resultado()

    def generarNaturaleza(self):
        return AnimalNaturaleza("Animal")

    def generarNaturalezaRobot(self):
        return RobotNaturaleza("Robot")

    def generarNaturalezaCosa(self):
        return CosaNaturaleza("Cosa")

    def generarNaturalezaCompuesto(self):
        return CompuestoNaturalezas()

    def generarAtaqueAtaqueCanionSonico(self):
        return AtaqueCanionSonico(4, 1)

    def generarAtaqueAtaqueGarraMecanica(self):
        return AtaqueGarraMecanica(2, 2)

    def generarAtaqueAtaquePomadaWassington(self):
        return AtaquePomadaWassington(5, 1)

    def generarAtaqueRayoVeloz(self):
        return AtaqueRayoVeloz(3, 1)

    def generarAtaqueZapatazo(self):
        return AtaqueZapatazo(1, 3)
