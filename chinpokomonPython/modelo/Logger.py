from this import d


class SingletonClass(object):

    def __init__(self, estado):
        self._estado = estado

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
