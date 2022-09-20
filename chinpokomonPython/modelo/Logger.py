
# class Estado(object):
#     "Clase que representa una persona."

#     def __init__(self, logger):
#         self._logger = logger

#     @property
#     def logger(self):
#         return self._logger

#     @logger.setter
#     def logger(self, logger):
#         self._logger = logger

#     def info2(self, mensaje):
#         pass

#     def warn2(self, mensaje):
#         pass

#     def error2(self, mensaje):
#         pass

#     def debug2(self, mensaje):
#         pass


# class Debug(Estado):
#     def info2(self, mensaje):
#         print("INFO: " + mensaje)

#     def warn2(self, mensaje):
#         print("WARN: " + mensaje)

#     def error2(self, mensaje):
#         print("ERROR: " + mensaje)

#     def debug2(self, mensaje):
#         print("DEBUG: " + mensaje)


# class Error(Estado):
#     def info2(self, mensaje):
#         pass

#     def warn2(self, mensaje):
#         pass

#     def error2(self, mensaje):
#         print("ERROR: " + mensaje)

#     def debug2(self, mensaje):
#         pass


# class Info(Estado):
#     def info2(self, mensaje):
#         print("INFO: " + mensaje)

#     def warn2(self, mensaje):
#         print("WARN: " + mensaje)

#     def error2(self, mensaje):
#         print("ERROR: " + mensaje)

#     def debug2(self, mensaje):
#         pass


# class Warn(Estado):
#     def info2(self, mensaje):
#         pass

#     def warn2(self, mensaje):
#         print("WARN: " + mensaje)

#     def error2(self, mensaje):
#         print("ERROR: " + mensaje)

#     def debug2(self, mensaje):
#         pass


# @singleton
# class Singleton(cls):

#     def __init__(self, estado):
#         self._estado = estado

#     def set_nivel

#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance

#     def debug(self, mensaje):
#         self._estado.debug2(mensaje)

#     def info(self, mensaje):
#         self._estado.info2(mensaje)

#     def warn(self, mensaje):
#         self._estado.warn2(mensaje)

#     def errorg(self, mensaje):
#         self._estado.error2(mensaje)


# singleton = Singleton(Debug())
# # estado = Estado(singleton)
# # new_singleton = SingletonClass()


# # print(singleton is new_singleton)

# # singleton.singl_variable = "Singleton Variable"
# # print(new_singleton.singl_variable)


# # singleton = SingletonClass(Debug)
# # estado = Estado(singleton)
# print(singleton.info("probando"))

def singleton(cls):

    instances = dict()

    def decorar(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return decorar


@singleton
class Logger(object):

    def __init__(self, estado):
        self.__estado = estado

    def set_nivel(self, estado):
        self.__estado = estado

    def getInstance(self):
        return self.__estado

    def debug(self, string):
        self.__estado.debug2(string)

    def info(self, string):
        self.__estado.info2(string)

    def warn(self, string):
        self.__estado.warn2(string)

    def error(self, string):
        self.__estado.error2(string)
