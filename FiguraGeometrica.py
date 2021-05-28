# ABC: abstract base clase
# para crear una clse abtracta hay que heredear de abc
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, altura, ancho):
        if altura >= 0:           # Validando que alto y ancho sean positivos
            self._altura = altura
        else:
            self._altura = 0
        if ancho >= 0:
            self._ancho = ancho
        else:
            self._ancho = 0

    @property
    def altura(self):
        return self._altura

    @property
    def ancho(self):
        return self._ancho

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    def __str__(self):
        return f'altura: {self._altura} ancho: {self._ancho}'

    @abstractmethod
    def area(self):
        pass
