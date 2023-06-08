from classVehiculo import Vehiculo

class Nuevo(Vehiculo):
    __marca = 'Toyota'
    __version: str
    def __init__(self, mod, p, c, pb, version):
        super().__init__(mod, p, c, pb)
        self.__version = version
    
    def mostrar(self):
        super.mostrar()
        print(self.__version)
    
    def getmarca(self):
        return self.__marca
    def getversion(self):
        return self.__version
    
    def ImporteVenta(self):
        importe = self.getPrecioBase() + self.getPrecioBase() * 0.10
        if self.__version == 'full':
            importe += self.getPrecioBase() * 0.02
        return importe