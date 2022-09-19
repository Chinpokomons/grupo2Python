class ArenaDeBatalla:

    def __init__(self,chinpokomon1,chinpokomon2):
        self._chinpokomon1 = chinpokomon1
        self._chinpokomon2 = chinpokomon2

    def chinpokomon1(self):
        return self._chinpokomon1
    
    def chinpokomon2(self):
        return self._chinpokomon2

    def pelear(self,log):
        while(self.noTerminoLaPelea()):
            self._chinpokomon1.ataque(self._chinpokomon2)
            log.info("ataco " +self._chinpokomon1.nombre()+" ,La vida que tiene que tiene es " + self._chinpokomon1.vida()+ " y la vida de "+ self._chinpokomon2.nombre() + " es " + self._chinpokomon2.vida())
            self._chinpokomon2.ataque(self._chinpokomon1)
            log.info("ataco " +self._chinpokomon2.nombre()+" ,La vida que tiene que tiene es " + self._chinpokomon2.vida()+ " y la vida de "+ self._chinpokomon1.nombre() + " es " + self._chinpokomon1.vida())

    def noTerminoLaPelea(self):
        return not self.murioChinpokomon1() and not self.murioChinpokomon2()

    def murioChinpokomon1(self):
        return self._chinpokomon1.vida() <= 0
    
    def murioChinpokomon2(self):
        return self._chinpokomon2.vida() <= 0

    def chinpokomonGanador(self):
        if(self.murioChinpokomon1()):
            return self._chinpokomon2
        else:
            return self._chinpokomon1
    
    def imprimirChinpokomonGanador(self,log,chinpoGanador):
        log.error("El ganador es " + chinpoGanador.nombre() )

    def toString(self):
        return "ArenaDeBatalla [chinpokomon1=" + self._chinpokomon1 + ", chinpokomon2=" + self._chinpokomon2 + "]"