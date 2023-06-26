
class Curso:
    __id: int
    __anio: int
    __division: str

    def __init__(self, id, anio, division):
        self.__id = id
        self.__anio = anio
        self.__division = division
    
    def getId(self):
        return self.__id
    def getAnio(self):
        return self.__anio
    def getDivision(self):
        return self.__division
        