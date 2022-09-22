class ArenaDeBatalla:
    
    def __init__(self, chinpokomon1, chinpokomon2):
        self.__chinpokomon1 = chinpokomon1
        self.__chinpokomon2 = chinpokomon2

    @property
    def chinpokomon1(self):
        return self.__chinpokomon1

    @chinpokomon1.setter
    def chinpokomon1(self,nuevo):
      self.__chinpokomon1 = nuevo
    
    @property
    def chinpokomon2(self):
        return self.__chinpokomon2
    
    @chinpokomon2.setter
    def chinpokomon2(self,nuevo):
      self.__chinpokomon2 = nuevo

    def pelear(self, log):
        while(self.noTerminoLaPelea()):
            self.chinpokomon1.ataque(self.chinpokomon2)
            log.info("ataco " + self.chinpokomon1.nombreInChinpokomon)
            self.chinpokomon2.ataque(self.chinpokomon1)
            log.info("ataco " + self.chinpokomon2.nombreInChinpokomon)
        self.imprimirChinpokomonGanador(log, self.chinpokomonGanador())

    def noTerminoLaPelea(self):
        return not self.murioChinpokomon1() and not self.murioChinpokomon2()

    def murioChinpokomon1(self):
        return self.chinpokomon1.vidaInChinpokomon <= 0

    def murioChinpokomon2(self):
        return self.chinpokomon2.vidaInChinpokomon <= 0

    def chinpokomonGanador(self):
        if(self.murioChinpokomon1()):
            return self.chinpokomon2
        else:
            return self.chinpokomon1

    def imprimirChinpokomonGanador(self, log, chinpoGanador):
        log.error("El ganador es " + chinpoGanador.nombreInChinpokomon)

    def toString(self):
        return "ArenaDeBatalla [chinpokomon1=" + self.chinpokomon1.nombreInChinpokomon + ", chinpokomon2=" + self.chinpokomon2.nombreInChinpokomon + "]"
