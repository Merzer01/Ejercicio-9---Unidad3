from classLista import Lista
from classVehiculo import Vehiculo
from classNuevo import Nuevo
from classUsado import Usado
import unittest

class TestVehiculos(unittest.TestCase):
    def TestInsertar(self):
        lista = Lista()
        vehiculo1 = Nuevo('Sentra', 4, 'Azul', 350000, 'full')
        vehiculo2 = Usado('Uno', 4, 'Verde', 500000, 'AJ350', 'Fiat', 2003, 130000)

        lista.insertarElemento(vehiculo1, 0)
        self.assertEqual(len(lista), 1)
        self.assertEqual(lista.mostrarElemento(0), vehiculo1)

        lista.insertarElemento(vehiculo2, 2)
        self.assertEqual(len(lista), 3)
        self.assertEqual(lista.mostrarElemento(2), vehiculo2)

        with self.assertRaises(ValueError):
            lista.insertarElemento(vehiculo1, 5)
    
    def testAgregarElemento(self):
        lista = Lista()
        vehiculo1 = Nuevo("Corolla", 4, "Azul", 1500000, 'full')
        vehiculo2 = Usado('C4', 5, "Rojo", 1000000, 'AFJ 310J', 'Citroen', 2011, 90000)

        lista.agregarElemento(vehiculo1)
        self.assertEqual(len(lista), 1)
        self.assertEqual(lista.mostrarElemento(0), vehiculo1)

        lista.agregarElemento(vehiculo2)
        self.assertEqual(len(lista), 2)
        self.assertEqual(lista.mostrarElemento(1), vehiculo2)

    def testObtenerObjetoEnPosicion(self):
        lista = Lista()
        vehiculo1 = Nuevo('Kicks', 5, "Verde", 200000, 'full')
        vehiculo2 = Usado("Gol", 4, "Rojo", 1000000, 'AHM 318K', 'Volkswagen', 1999, 109000)

        lista.agregarElemento(vehiculo1)
        lista.agregarElemento(vehiculo2)

        self.assertEqual(lista.obtenerElementoEnPosicion(0), vehiculo1)
        self.assertEqual(lista.obtenerElementoEnPosicion(1), vehiculo2)

    def testModificarPrecioVenta(self):
        lista = Lista()
        vehiculo1 = Usado('A5', 4, 'Blanco', 2000000, 'CIG 873A', 'AUDI', 1999, 249000)

        lista.agregarElemento(vehiculo1)

        patente = vehiculo1.getPatente()
        precioFinal = lista.VentaPatente (patente)

        self.assertEqual(vehiculo1.getPrecioVenta(), precioFinal)

if __name__ == '__main__':
    unittest.main()