
class Preceptor:
    __id: int
    __nombre: str
    __apellido: str
    __correo: str
    __clave: str

    def __init__(self, id, nombre, apellido, correo, clave):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__clave = clave
    
    def getId(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getCorreo(self):
        return self.__correo
    def getClave(self):
        return self.__clave
        