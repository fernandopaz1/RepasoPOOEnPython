class MiClase:
    # Las variables de instancia se definen fuera de cualquier metodo
    # pero dentro de la csale
    variables_clase = 'Valor de la variable de clase'

    def __init__(self, variable_instancia):
        self._variable_instancia = variable_instancia

    # Lo metodos estaticos se asocian con la clase y no con los objetos
    # Como no puede acceder a las variables de instancia
    # no recibe como parametro el self
    # Esto se conoce como contexto estatico
    @staticmethod
    def metodoEstatico():
        print(MiClase.variables_clase)  # Puedo acceder a las variables de clase

    @classmethod
    def metodo_clase(cls):
        # Con cls podemos acceder a las variables de clase sin llam raa la clase en si
        print(cls.variables_clase)

    # Los metodos de instancia pueden acceder tanto a los metodos de clase
    # como a los metodos de instancia, debido a que el contexto dinamico
    # puede acceder al contexto estatico
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodoEstatico()
        print(self.variables_clase)
        print(self._variable_instancia)


# Las variables de clase se acceden desde la clase
# no necesario crear una clase para saber su valor
# esta asociada a la clase y no necesariamente a los objetos
print(MiClase.variables_clase)

# Tambien podemos acceder a las variables de clase desde los objetos
miClase = MiClase("valor de valriable de instancia")
print(miClase.variables_clase)

# Podemos crear variables de clase fuera de la clase
# Podemos incluso accederla desde objeto creados previamente a
# la asignacion de est nueva variable
MiClase.variables_clase2 = 'Nueva variable de clase'
print(miClase.variables_clase2)

# Cuando se llama a un metodo de clase no se pasa como parametro
# a cls similar a como funciona self
print(MiClase.metodo_clase())

# Si bien desde el contexto estatico no puedo acceder al estatico
# desde el dinamico (objetos) puedo acceder al estatico, y que se crea lu
# posteriormente
miClase2 = MiClase("Variable del objeto 2")
print(miClase2.metodo_clase())
