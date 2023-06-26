
class Asistencia:
    __fecha: str
    __codigoClase: int
    __asistio: bool
    __justificacion: str

    def __init__(self, fecha, codigoClase, asistio, justificacion):
        self.__fecha = fecha
        self.__codigoClase = codigoClase
        self.__asistio = asistio
        self.__justificacion = justificacion

    def getFecha(self):
        return self.__fecha

    def getCodigoClase(self):
        return self.__codigoClase
    
    def getAsistio(self):
        return self.__asistio
    
    def getJustificacion(self):
        return self.__justificacion