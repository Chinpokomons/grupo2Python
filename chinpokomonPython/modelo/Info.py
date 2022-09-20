from Estado import Estado


class Info(Estado):
    def info2(self, mensaje):
        print("INFO: " + mensaje)

    def warn2(self, mensaje):
        print("WARN: " + mensaje)

    def error2(self, mensaje):
        print("ERROR: " + mensaje)

    def debug2(self, mensaje):
        return
