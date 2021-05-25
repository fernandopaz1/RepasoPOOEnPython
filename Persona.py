class Persona:
    # Para utilizar atributos en una clase es necesario el metodo
    # init, es un metodo inicializador. Es similar a un constructor,
    # solo que le metodo constructor esta oculta y se manda a llama
    # por el lenguaje. init nos permite agrgar artibutos e inicializarlos
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        # self (es como this) es una referencia al objeto que se va a crear
        # el __ al inicia y al final lo hacen un metodo especial (tipo dunder)
        # el init recibe como parametros las variables de instancia del objeto
        # self apunta a la direccion de memoria del objeto que se esta creando
        self._nombre = nombre  # con atributos que empiecen con _ indicamos que son privados
        self.__apellido = apellido  # Con __ indicamos que no pueden ser modificadoes
        self._edad = edad
        self._args = args  # Agregando argumentos variables y diccionarios
        self._kwargs = kwargs  # se puede robustecer el metodo init
        pass

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.__apellido} {self._edad} {self._args} {self._kwargs}')

    @property  # El decorador hace que pueda acceder a nombre como si fuera un atributo
    def nombre(self):
        return self._nombre  # de manera indirecta estaremos llamando al metodo

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Si dejamos _edad y no le hacemos un metodo setter es un tributo read only
    # ya que no se puede modificar con la sintaxis persona1.edad = ...

    # def __del__(self):  # Para eliminaar un objeto hay que usar el metodo
        # __del__ herdado de la clase object, no es algo que se use mucho ya que
        # python cuenta con garbage collector. Se llama como del nombreObjeto
        # print(f'Eliminando: {self._nombre} {self.__apellido}')

    # Sobreescribiendo el metodo __str__ de object
    def __str__(self, *args, **kwargs):  # Cuando hacemos print manda a llamar este metodo
        return f'{self._nombre} {self.__apellido} {self._edad}'

    pass  # indica que no se procesa nada mas y se crea
    # el tipo de dato
    # Se usa tambien para crear funciones sin contenido


# El __name__ es tal que si esta en el archivo principal en ejecucion
# __name__ devuelve __main__, si no es el archivo principal devuelve
# el nombre del archivo

# El codigo de abajo solo se ejecuta si Persona es el archivo principal
if __name__ == '__main__':
    print(__name__)

    print(type(Persona))  # Persona es de tipo clase

    persona1 = Persona('Juan', 'Perez', 28)  # se crea un objeto y se llama al metodo __init__
    # El self se pasa automatcamente al init no es necesario ponerlo
    print(persona1)  # imprime la direccion de memeoria del objeto
    persona1.mostrar_detalle()
    persona2 = Persona('Maria', 'Perez', 29)
    persona2.mostrar_detalle()

    # El metodo puede ser llamado tambien sobre la clase
    # pero hay que pasarle el objeto que queremos como parametro
    # lo mas comun es hacerlo con la otra notacion
    Persona.mostrar_detalle(persona1)

    persona1.telefono = '55441122'
    # Le podemos seguir agregando argumentos a los objetos, pero
    # estos atributso no los van a tener los objetos de la misma clase

    print(persona1.telefono)

    persona3 = Persona('Azdrubal', 'Perez', 24, 4, 56, 6, 67, m='manzana', n='naranja')
    persona3.mostrar_detalle()

    print(persona1.nombre)  # Llama al metodo nombre dentro de la clase
    persona1.nombre = 'Fernando'  # Llama a setter de la clase Persona
    print(persona1.nombre)
