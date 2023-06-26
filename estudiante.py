
class Estudiante:
    __id: int
    __nombre: str
    __apellido: str
    __dni: str

    def __init__(self, id, nombre, apellido, dni):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
    
    def getId(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDni(self):
        return self.__dni