class Chinpokomon():

    #aca irian los atributos, agregar property
    def __init__(self):
        self.nombre = None
        self.vida = None
        self.listaAtaques = []
        self.naturaleza = None

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setVida(self,vida):
        self.vida = vida

    def setAtaques(self,listaDeAtaques):
        self.ataques = listaDeAtaques

    def setNaturaleza(self,naturaleza):
        self.naturaleza = naturaleza
    

    def ataque(self,unChimpokomon):
        if (self.noEstaMuertoOtroChimpokomon(unChimpokomon) and self.estoyVivo()):
            self.ataca 
            "seguir con el codigo"
        

    def atacarSegunAtaqueSeleccionado(self,chimpokomonAAtacar):
        if(self.getAtaques().size() == 1):
            self.getAtaques().get(0).generarEfecto(self, chimpokomonAAtacar)
        else:
            "seguir con el codigo"
        

    def estoyVivo(self):
        return self.getVida() > 0

    def noEstaMuertoOtroChimpokomon(self,chimpokomon):
        return chimpokomon.getVida() > 0
    