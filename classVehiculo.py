import abc
from abc import ABC

class Vehiculo(ABC):
    def __init__(self, mod, p ,c, pb):
        self.__modelo = mod
        self.__puertas = p
        self.__color = c
        self.__precioBase = pb

    def mostrar(self):
        print('{} {} {} {} - '.format(self.__modelo, self.__puertas, self.__color, self.__precioBase, self.ImporteVenta()))
    
    @abc.abstractclassmethod
    def ImporteVenta():
        pass
    
    def getmodelo(self):
        return self.__modelo
    def getpuerta(self):
        return self.__puertas
    def getcolor(self):
        return self.__color
    def getprecio(self):
        return self.__precioBase