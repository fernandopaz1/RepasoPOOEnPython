from OrdenProducto.Producto import Producto


class Orden:
    contador_ordenes = 0
    
    def __init__(self):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = []


    def __str__(self):
        return f'{self._id_orden} Productos: {self._productos}'


        