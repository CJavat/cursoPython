"""
    Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. 
    El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas
"""

vocalMinuscula = input("Escribe una vocal en minuscula: ")
vocalMayuscula = input("Escribe una vocal en mayuscula: ")

print("Vocal convertida en MAYUSCULA: ", vocalMinuscula.swapcase(), " y Vocal convertida en MINUSCULA: ", vocalMayuscula.swapcase())