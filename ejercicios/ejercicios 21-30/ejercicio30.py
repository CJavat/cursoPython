"""
    Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
    Calcular después la suma, resta, multiplicación y división. 
    Utilizar un método para cada una e imprimir los resultados obtenidos. 
    Llamar a la clase Calculadora.
"""

class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        resultado = self.numero1 + self.numero2
        print("El resultado de la suma es: {}".format(resultado))
    
    def restar(self):
        resultado = self.numero1 - self.numero2
        print("El resultado de la resta es: {}".format(resultado))
    
    def multiplicar(self):
        resultado = self.numero1 * self.numero2
        print("El resultado de la multiplicacion es: {}".format(resultado))
    
    def dividir(self):
        if self.numero2 == 0:
            print("No se puede dividir entre 0.")
        else:
            resultado = self.numero1 / self.numero2
            print("El resultado de la division es: {}".format(resultado))

num1 = int(input("Introduce el numero 1: "))
num2 = int(input("Introduce el numero 2: "))

suma = Calculadora(num1, num2)
resta = Calculadora(num1, num2)
multiplicacion = Calculadora(num1, num2)
division = Calculadora(num1, num2)

suma.sumar()
resta.restar()
multiplicacion.multiplicar()
division.dividir()