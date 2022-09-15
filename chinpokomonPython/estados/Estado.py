class Estado(object):
    "Clase que representa una persona."

    def __init__(self, logger):
        self._logger = logger

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, logger):
        self._logger = logger

    def info2(self, mensaje):
        pass

    def warn2(self, mensaje):
        pass

    def error2(self, mensaje):
        pass

    def debug2(self, mensaje):
        pass
