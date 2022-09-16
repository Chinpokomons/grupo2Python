
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


class Debug(Estado):
    def info2(self, mensaje):
        print("INFO: " + mensaje)

    def warn2(self, mensaje):
        print("WARN: " + mensaje)

    def error2(self, mensaje):
        print("ERROR: " + mensaje)

    def debug2(self, mensaje):
        print("DEBUG: " + mensaje)


class Error(Estado):
    def info2(self, mensaje):
        pass

    def warn2(self, mensaje):
        pass

    def error2(self, mensaje):
        print("ERROR: " + mensaje)

    def debug2(self, mensaje):
        pass


class Info(Estado):
    def info2(self, mensaje):
        print("INFO: " + mensaje)

    def warn2(self, mensaje):
        print("WARN: " + mensaje)

    def error2(self, mensaje):
        print("ERROR: " + mensaje)

    def debug2(self, mensaje):
        pass


class Warn(Estado):
    def info2(self, mensaje):
        pass

    def warn2(self, mensaje):
        print("WARN: " + mensaje)

    def error2(self, mensaje):
        print("ERROR: " + mensaje)

    def debug2(self, mensaje):
        pass


class SingletonClass(object):

    def __init__(self):
        self._estado = Debug()

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

    def debug(self, mensaje):
        self._estado.debug2(mensaje)

    def info(self, mensaje):
        self._estado.info2(mensaje)

    def warn(self, mensaje):
        self._estado.warn2(mensaje)

    def errorg(self, mensaje):
        self._estado.error2(mensaje)


singleton = SingletonClass()
new_singleton = SingletonClass()


print(singleton is new_singleton)

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)

singleton = SingletonClass()
print(singleton.info("probando"))
