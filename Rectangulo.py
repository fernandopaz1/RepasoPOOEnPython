from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Rectangulo(FiguraGeometrica, Color):
    # Con 3 comillaso dobles hacemos un comentario especial
    # que sirve como documentacion
    """"
    Clase de rectangulos
    """

    def __init__(self, altura, ancho, color):
        FiguraGeometrica.__init__(self, altura, ancho)
        Color.__init__(self, color)

    def area(self):
        return self._ancho * self._altura

    def perimetro(self):
        return 2 * (self._ancho + self._altura)

    def imprimir_area(self):
        print(f"Área rectángulo: {self.area()}")

    pass

    def __str__(self):
        return f'Rectanglo de ' + FiguraGeometrica.__str__(self)


if __name__ == '__main__':
    ancho = int(input("Proporciona la base: "))
    altura = int(input("Proporciona la altura: "))

    rectangulo1 = Rectangulo(altura, ancho, 'amarillo')

    rectangulo1.imprimir_area()
