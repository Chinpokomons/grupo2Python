from ArenaBatalla import ArenaDeBatalla
from BuilderOfChinpokomon import BuilderOfChinpokomon
from GeneradorDeChinpokomon import GeneradorDeChinpokomon
from Logger import Logger
from Error import Error
from Info import Info
from Warn import Warn
from Debug import Debug

def main():

    # //punto 1
    # info = Info()
    # warn = Warn()
    # error = Error()
    debug = Debug()

    # loggerSingleton = Logger(info)
    loggerSingleton = Logger(debug)
    builder = BuilderOfChinpokomon()
    generador = GeneradorDeChinpokomon(builder)
    zapatito = generador.buildZapato()
    gallotronix = generador.buildGallotronix()
    print(
        "!-------------------punto 1-------------------------------------!")
    loggerSingleton.debug("lA VIDA DEL CHINPOKOMON " + zapatito.nombreInChinpokomon +
                         " AL EMPEZAR ES: " + str(zapatito.vidaInChinpokomon))
    print("-------------")
    loggerSingleton.debug("lA VIDA DEL CHINPOKOMON " +
                         gallotronix.nombreInChinpokomon + " AL EMPEZAR ES: " + str(gallotronix.vidaInChinpokomon))

    print("-------------")

    arena1 = ArenaDeBatalla(zapatito, gallotronix)
    arena1.pelear(loggerSingleton)

    # //punto 4
    print(
        "!-------------------punto 4-------------------------------------!")
    zapatoEspecial = generador.buildZapatoEspecial()
    carnotron = generador.buildCarnotron()
    
    loggerSingleton.debug("lA VIDA DEL CHINPOKOMON " + zapatoEspecial.nombreInChinpokomon +
                         " AL EMPEZAR ES: " + str(zapatoEspecial.vidaInChinpokomon))
    print("-------------")
    loggerSingleton.debug("lA VIDA DEL CHINPOKOMON " +
                         carnotron.nombreInChinpokomon + " AL EMPEZAR ES: " + str(carnotron.vidaInChinpokomon))

    print("-------------")

    arena2 = ArenaDeBatalla(zapatoEspecial, carnotron)
    arena2.pelear(loggerSingleton)


main()
