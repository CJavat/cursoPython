"""
    6 - Definir una función inversa() que calcule la inversión de una cadena. 
    Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(cadena):
    cadenaInversa = cadena[: : -1]
    print(cadenaInversa)

texto = input("Escribe un texto para invertirlo: ")

inversa(texto)