
class Curso:
    __idCurso: int
    __anio: int
    __division: str

    def __init__(self, idCurso, anio, division):
        self.__idCurso = idCurso
        self.__anio = anio
        self.__division = division
    
    def getIdCurso(self):
        return self.__idCurso
    def getAnio(self):
        return self.__anio
    def getDivision(self):
        return self.__division
