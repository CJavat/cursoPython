# INTRODUCCIÓN A FUNCIONES.

# FUNCIONES PROPIAS DE PYTHON.
num = "70"

print(type(num))
print(type(int(num)))
print(type(float(num)))

lista = [12, 60, 70, 1, -2]

print(len(lista)) # DEVUELVE LA LONGITUD.
print(max(lista)) # DEVUELVE EL VALOR MÁXIMO.
print(min(lista)) # DEVUELVE EL VALOR MÍNIMO.

# DECLARAR FUNCIONES.
""" 
    def nombreFuncion():
        sentencia
"""

# MANDAR A LLAMAR A LA FUNCIÓN:
# nombreFuncion()

def saludo():
    print("Hola mundo con función")

# saludo()

def tabla7():
    for i in range(1, 11):
        print("7 X ", i, " = ", i*7)

# tabla7()

# FUNCIONES MATEMÁTICAS
import math
import random

print(math.pow(10, 2)) # DEVUELVE EL EXPONENTE
print(math.sqrt(64)) # DEVUELVE LA RAIZ CUADRADA EN FLOAT
print(math.isqrt(64)) # DEVUELVE LA RAIZ CUADRADA EN INT
print(math.sin(90)) # DEVUELVE EL SENO
print(math.cos(90)) # DEVUELVE EL COSENO
print(math.tan(90)) # DEVUELVE LA TANGENTE
print(math.factorial(4)) # DEVUELVE EL FACTORIAL

print(random.randint(1, 100)) # DEVUELVE UN NUMERO ALEATORIO

# RETURN DE FUNCIONES
def entero():
    print("Este es un dato entero: ")
    return 10

def decimal():
    print("Este es un dato decimal: ")
    return 90.99

def frase():
    print("Esta es una frase:")
    return "Hola Mundo"

print(entero()) # PARA MOSTRAR EL DATO DEL RETURN SE DEBE DE IMPRIMIR
print(decimal())
print(frase())

# FORMA DE ASGINARLE VALOR A LAS VARIABLES CON UN RETURN EN UNA FUNCION
def asignacion():
    return 1, 2, 3, 4, 5

a, b, c, d, e = asignacion()
print(a, b, c, d, e)

# PARAMETROS Y FUNCIONES
def suma(num1, num2):
    sumar = num1 + num2
    return sumar

print(suma(10, 5))

# VARIBLES GLOBALES
def valores():
    global numero1
    global numero2
    numero1 = 10
    numero2 = 5
    return numero1 - numero2
valores()

resta = numero1 - numero2
print(resta)

# ARGUMENTOS INDEFINIDOS

def argumentos(*num): # DECLARACIÓN DE UNA TUPLA.
    return type(num)

print(argumentos(10, 4))

