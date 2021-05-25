class Aritmetica:
    # Con 3 comillaso dobles hacemos un comentario especial
    # que sirve como documentacion
    """"
    Clase de aritmetica para realizar operaciones de sumar,
    restar, etc.
    """

    def __init__(self, operando_a, operando_b):
        self.operandoA = operando_a
        self.operandoB = operando_b
        pass

    def suma(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        if self.operandoB != 0:
            return self.operandoA / self.operandoB
        else:
            print("Error no se puede dividir por cero")

    pass


aritmetica1 = Aritmetica(5, 3)

aritmetica2 = Aritmetica(3, 0)

print(aritmetica1.suma())

print(aritmetica1.resta())

print(aritmetica2.dividir())
