from ArenaBatalla import ArenaDeBatalla
# from Ataque import Ataque
# from AtaqueCanionSonico import AtaqueCanionSonico
# from AtaqueGarraMecanica import AtaqueGarraMecanica
# from AtaquePomadaWassington import AtaquePomadaWassington
# from AtaqueRayoVeloz import AtaqueRayoVeloz
# from AtaqueZapatazo import AtaqueZapatazo
# from Builder import Builder
from BuilderOfChinpokomon import BuilderOfChinpokomon
# from Chinpokomon import Chinpokomon
# from CompuestoNaturalezas import CompuestoNaturalezas
# from CosaNaturaleza import CosaNaturaleza
# from GeneracionDeRandom import GeneracionDeRandom
from GeneradorDeChinpokomon import GeneradorDeChinpokomon
# from InterfaceNaturaleza import InterfaceNaturaleza
from Logger import Logger
# from Naturaleza import Naturaleza
# from RobotNaturaleza import RobotNaturaleza
# from Debug import Debug
from Error import Error
# from Estado import Estado
from Info import Info
from Warn import Warn


def main():

    # //punto 1
    # info = Info()
    # warn = Warn()
    # error = Error()

    # loggerSingleton = Logger(info)
    loggerSingleton = Logger(Info())
    builder = BuilderOfChinpokomon()
    generador = GeneradorDeChinpokomon()
    generador.builder = builder
    zapatito = generador.crearZapato(builder)
    gallotronix = generador.crearGallotronix(builder)
    print(
        "!-------------------punto 1-------------------------------------!")
    loggerSingleton.info("lA VIDA DEL ZAPATO " + zapatito +
                         " AL EMPEZAR ES: " + zapatito.getVida())
    print("-------------")
    loggerSingleton.info("lA VIDA DEL gallotronix " +
                         gallotronix + " AL EMPEZAR ES: " + gallotronix.getVida())

    print("-------------")

    arena1 = ArenaDeBatalla(zapatito, gallotronix)
    print(arena1)
    arena1.pelea(loggerSingleton)

    # //punto 4
    print(
        "!-------------------punto 4-------------------------------------!")
    zapatoEspecial = generador.crearZapatoConDosAtaques(builder)

    loggerSingleton.info("lA VIDA DEL ZAPATO " + zapatoEspecial +
                         " AL EMPEZAR ES: " + zapatito.getVida())
    print("-------------")
    loggerSingleton.info("lA VIDA DEL gallotronix " +
                         gallotronix + " AL EMPEZAR ES: " + gallotronix.getVida())

    print("-------------")

    arena2 = ArenaDeBatalla(zapatoEspecial, gallotronix)
    print(arena2)
    arena2.pelea(loggerSingleton)


main()
