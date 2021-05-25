from Cuadrado import *
from Rectangulo import *

cuadrado1 = Cuadrado(5, 'rojo')
rectangulo1 = Rectangulo(2, 3, 'Amarillo')

print(f'El area del cuadrado es {cuadrado1.area()}')

# MRO : method resolution order
# Es un  metodo que nos dice en que orden sejecutan los metodos
# segun la jerarquia de clases que
# Se ejecuta el primer metodo que se encuentre
# Esto se puede modificar cambiando el orden de los argumentos
# de la clase
print(Cuadrado.mro())

print(rectangulo1)
print(cuadrado1)