from Estado import Estado


class Error(Estado):
    def info2(self, mensaje):
        return

    def warn2(self, mensaje):
        return

    def error2(self, mensaje):
        print("ERROR: " + mensaje)

    def debug2(self, mensaje):
        return
