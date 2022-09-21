class ArenaDeBatalla:

    def __init__(self, chinpokomon1, chinpokomon2):
        self.chinpokomon1 = chinpokomon1
        self.chinpokomon2 = chinpokomon2

    @property
    def chinpokomon1(self):
        return self.chinpokomon1

    @property
    def chinpokomon2(self):
        return self.chinpokomon2

    def pelear(self, log):
        while(self.noTerminoLaPelea()):
            self.chinpokomon1.ataque(self._chinpokomon2)
            log.info("ataco " + self.chinpokomon1.getNombre())
            self.chinpokomon2.ataque(self._chinpokomon1)
            log.info("ataco " + self._chinpokomon2.getNombre())
        self.imprimirChinpokomonGanador(log, self.chinpokomonGanador())

    def noTerminoLaPelea(self):
        return not self.murioChinpokomon1() and not self.murioChinpokomon2()

    def murioChinpokomon1(self):
        return self.chinpokomon1().vida() <= 0

    def murioChinpokomon2(self):
        return self.chinpokomon2().vida() <= 0

    def chinpokomonGanador(self):
        if(self.murioChinpokomon1()):
            return self.chinpokomon2
        else:
            return self.chinpokomon1

    def imprimirChinpokomonGanador(self, log, chinpoGanador):
        log.error("El ganador es " + chinpoGanador.getNombre())

    def toString(self):
        return "ArenaDeBatalla [chinpokomon1=" + self._chinpokomon1 + ", chinpokomon2=" + self._chinpokomon2 + "]"
