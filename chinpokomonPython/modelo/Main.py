from ArenaBatalla import ArenaDeBatalla
from BuilderOfChinpokomon import BuilderOfChinpokomon
from GeneradorDeChinpokomon import GeneradorDeChinpokomon
from Logger import Logger
from Error import Error
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
    generador = GeneradorDeChinpokomon(builder)
#    generador.builder = builder
    print(generador.builder)
    zapatito = generador.buildZapato()
    gallotronix = generador.buildGallotronix()
    print(
        "!-------------------punto 1-------------------------------------!")
    loggerSingleton.info("lA VIDA DEL ZAPATO " + zapatito.tostring() +
                         " AL EMPEZAR ES: " + str(zapatito.vidaInChinpokomon))
    print("-------------")
    loggerSingleton.info("lA VIDA DEL gallotronix " +
                         gallotronix.tostring() + " AL EMPEZAR ES: " + str(gallotronix.vidaInChinpokomon))

    print("-------------")

    arena1 = ArenaDeBatalla(zapatito, gallotronix)
    print(arena1)
    arena1.pelear(loggerSingleton)

    # //punto 4
    print(
        "!-------------------punto 4-------------------------------------!")
    zapatoEspecial = generador.buildZapatoEspecial()
    carnotron = generador.buildCarnotron()
    
    loggerSingleton.info("lA VIDA DEL ZAPATO " + zapatoEspecial.tostring() +
                         " AL EMPEZAR ES: " + str(zapatoEspecial.vidaInChinpokomon))
    print("-------------")
    loggerSingleton.info("lA VIDA DEL gallotronix " +
                         carnotron.tostring() + " AL EMPEZAR ES: " + str(carnotron.vidaInChinpokomon))

    print("-------------")

    arena2 = ArenaDeBatalla(zapatoEspecial, carnotron)
    print(arena2)
    arena2.pelear(loggerSingleton)


main()
