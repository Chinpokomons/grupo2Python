from estados.Estado import Estado


class Error(Estado):
    def info2(self, mensaje):
        pass

    def warn2(self, mensaje):
        pass

    def error2(self, mensaje):
        print("ERROR: " + mensaje)

    def debug2(self, mensaje):
        pass
