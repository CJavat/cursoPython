"""
    7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
    ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo(palabra):
    palabraInversa = palabra[: : -1]
    
    if palabraInversa == palabra:
        return True
    else:
        return False

palabra = input("Ingrese una palabra: ")

respuesta = es_palindromo(palabra)

print("Es palindromo?, {}".format(respuesta))