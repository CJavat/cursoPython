"""
    Escribir un programa que pregunte al usuario su edad 
    y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

edad = int(input("Introduce tu edad: "))

i = 1
while i <= edad:
    print("Cumpliste el año: ", i, '\n')
    i += 1