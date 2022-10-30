"""
    Escribir un programa que pida un numero al usuario 
    y muestre las tablas de multiplicar de ese numero
"""

numero = int(input("Escribe un numero: "))
i = 1
while i <= 10:
    print(numero, " X ", i, " = ", (numero*i))
    i += 1