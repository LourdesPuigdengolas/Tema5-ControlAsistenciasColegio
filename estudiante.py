
class Estudiante:
    __idEstud: int
    __nombre: str
    __apellidEstudo: str
    __dni: str

    def __init__(self, idEstud, nombre, apellidEstudo, dni):
        self.__idEstud = idEstud
        self.__nombre = nombre
        self.__apellidoEstud = apellidoEstud
        self.__dni = dni
    
    def getIdEstud(self):
        return self.__idEstud
    def getNombre(self):
        return self.__nombre
    def getApellidoEstud(self):
        return self.__apellidoEstud
    def getDni(self):
        return self.__dni