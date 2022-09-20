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
    print(generador.builder)
    zapatito = generador.buildZapato()
    gallotronix = generador.buildGallotronix()
    print(
        "!-------------------punto 1-------------------------------------!")
    loggerSingleton.info("lA VIDA DEL ZAPATO " + zapatito.toString() +
                         " AL EMPEZAR ES: " + str(zapatito.getVida()))
    print("-------------")
    loggerSingleton.info("lA VIDA DEL gallotronix " +
                         gallotronix.toString() + " AL EMPEZAR ES: " + str(gallotronix.getVida()))

    print("-------------")

    arena1 = ArenaDeBatalla(zapatito, gallotronix)
    print(arena1)
    arena1.pelear(loggerSingleton)

    # //punto 4
    print(
        "!-------------------punto 4-------------------------------------!")
    zapatoEspecial = generador.buildZapatoEspecial()
    carnotron = generador.buildCarnotron()
    
    loggerSingleton.info("lA VIDA DEL ZAPATO " + zapatoEspecial.toString() +
                         " AL EMPEZAR ES: " + str(zapatoEspecial.getVida()))
    print("-------------")
    loggerSingleton.info("lA VIDA DEL gallotronix " +
                         carnotron.toString() + " AL EMPEZAR ES: " + str(carnotron.getVida()))

    print("-------------")

    arena2 = ArenaDeBatalla(zapatoEspecial, carnotron)
    print(arena2)
    arena2.pelear(loggerSingleton)


main()
