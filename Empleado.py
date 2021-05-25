from Persona import Persona


class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, sueldo):
        super().__init__(nombre, apellido, edad)
        self._sueldo = sueldo

    # Al hacer el __str__ de una clase heredad usamos super
    # para rehutilizar el metodo de la clase padre
    def __str__(self, *args, **kwargs):
        return super().__str__() + f' Sueldo: ${self._sueldo}'


empleado1 = Empleado('Fernando', 'Paz', 28, 400)

print(empleado1)