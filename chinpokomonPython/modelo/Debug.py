from Estado import Estado


class Debug(Estado):
    def info2(self, mensaje):
        print("INFO: " + mensaje)

    def warn2(self, mensaje):
        print("WARN: " + mensaje)

    def error2(self, mensaje):
        print("ERROR: " + mensaje)

    def debug2(self, mensaje):
        print("DEBUG: " + mensaje)
