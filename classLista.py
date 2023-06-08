from Nodo import Nodo
from classNuevo import Nuevo
from classUsado import Usado
from interfaz import Interfaz
from zope.interface import implementer

@implementer(Interfaz)
class Lista:
    __comienzo: None
    __actual: None
    __indice = 0
    __tope = 0
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getdato()
            self.__actual = self.__actual.getsiguiente()
            return dato

    def agregarElemento(self, elemento):
        nodo = Nodo(elemento)   #CREAR NODO
        if self.__comienzo == None:
            self.__comienzo = nodo
        else: 
            aux = self.__comienzo
            while aux.getsig() != None:
                aux = aux.getsig()
    
    def insertarElemento(self, elemento, posicion): #opcion 2
        if posicion < 0 or posicion > self.__tope:
            raise ValueError('Posicion invalida')
        if posicion == 0:
            self.agregarElemento(elemento)
        else:
            self.__indice = 0
            anterior = self.searchAnt(posicion)
            nuevo = Nodo(elemento)
            sig = anterior.getsiguiente()
            nuevo.setsiguiente(sig)
            anterior.setsiguiente(Nodo)
            self.__actual = nuevo
            self.__tope += 1
            self.__indice = 0

    def mostrarElemento(self, posicion):
        aux = self.__comienzo
        i = 1
        while aux != None and i != posicion:
            i += 1
            aux = aux.getsig()
        if i == posicion:
            if isinstance (aux.getdato(), Nuevo):
                print("AUTO NUEVO")
            else: print("AUTO USADO")
        else: print("Esa posicion no esta en la lista")

    def precio_patente(self, pat):
        aux = self.__comienzo
        band = False
        while not band:
            if isinstance(aux.getdato(), Usado) and aux.getdato().getpatente():
                band = True
                precio = aux.getdat().ImporteVenta()
        return precio

    
    def economico(self):
        min = 9999999
        aux = self.__comienzo
        retorno = None
        while aux != None:
            if aux.getdato().ImporteVenta() < min:
                min = aux.getdato().ImporteVenta()
                retorno = aux.getdato()
            aux = aux.getsig()
        return retorno