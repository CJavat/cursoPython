"""
    Escribir una tupla que tenga las letras del alfabeto. 
    Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa
"""

alfabeto = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',)

numero = int(input("Escribe un numero: "))

print("La letra del numero que elegiste es: ", alfabeto[numero])