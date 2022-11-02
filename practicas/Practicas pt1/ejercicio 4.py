"""
    4 - Escribir una función que tome un carácter y devuelva True si es una vocal, 
    de lo contrario devuelve False.
"""

def vocalNoVocal(car):
    caracter = car.lower()
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        return True
    else:
        return False


caracter = input("Ingresa un caracter: ")

respuesta = vocalNoVocal(caracter)

print("El resultado es: {}".format(respuesta))