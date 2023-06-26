from curso import Curso

class Preceptor:
    __idPrece: int
    __nombre: str
    __apellidoPrece: str
    __correo: str
    __clave: str

    def __init__(self, idPrece, nombre, apellidoPrece, correo, clave):
        self.__idPrece = idPrece
        self.__nombre = nombre
        self.__apellidoPrece = apellidoPrece
        self.__correo = correo
        self.__clave = clave
    
    def getidPrece(self):
        return self.__idPrece
    def getNombre(self):
        return self.__nombre
    def getApellidoPrece(self):
        return self.__apellidoPrece
    def getCorreo(self):
        return self.__correo
    def getClave(self):
        return self.__clave
