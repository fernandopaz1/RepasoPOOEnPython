# operador + esta sobrecargado: depende si sumamos strings o ints

a = 1
b = 2
print(a + b)

c = 'Hola '
d = ' Mundo!'
print(c + d)
e = [1, 2, 'Hola']
f = ['a', 3, 1]
print(e + f)

# Si queremos sobreescribir la suma creamos en nuestra
# clas el metodo __add__(self, other) y 
# __sub__(self, other) para sobreescribir la resta 
