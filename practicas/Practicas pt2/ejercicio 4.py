"""
    Escribir un programa que le diga al usuario que ingrese una cadena. 
    El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

cadena = input("Ingresa una cadena: ")

abecedarios = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
contadorLetras = 0
contadorMayusculas = 0

while contadorLetras < len(cadena):
    for i in abecedarios:
        if cadena[contadorLetras] == i:
            contadorMayusculas += 1
    
    contadorLetras += 1

print("El numero total de mayusculas en la cadena es de: {}".format(contadorMayusculas))