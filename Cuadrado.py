from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super().__init__() no se usa esto por ser ambiguo
        FiguraGeometrica.__init__(self, lado, lado)  # Hay que pasar self
        Color.__init__(self, color)

    def area(self):
        return self._altura * self._ancho

    def __str__(self):
        return f'Cuadrado de lado: {self._ancho}'
