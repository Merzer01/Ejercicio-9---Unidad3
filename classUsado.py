from classVehiculo import Vehiculo
from datetime import datetime

class Usado(Vehiculo):
    __patente: str
    __año: int
    __kilometraje: int
    __marca: str
    def __init__(self, mod, p, c, pb, pat, marca, año, km):
        super().__init__(mod, p, c, pb)
        self.__patente = pat
        self.__año = año
        self.__marca = marca
        self.__kilometraje = km

    
    def ImporteVenta(self):
        fecha = datetime.now().date()
        actual = fecha.year
        importe = self.__precioBase - (actual - self.__año)*0.01
        if self.__kilometraje > 100000:
            importe -= self.__precioBase * 0.02
        return importe
    
    def mostrar(self):
        super.mostrar()
        print("etc")

    def getpatente(self):
        return self.__patente
    def getaño(self):
        return self.__año
    def getkm(self):
        return self.__kilometraje
    def getmarca(self):
        return self.__marca