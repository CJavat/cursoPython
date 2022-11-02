"""
    8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común 
    o devuelva False de lo contrario. 
    Escribir la función usando el bucle for anidado.
"""

def superposicion(lista1, lista2):
    encontrado = False
    for i in lista1:
        for j in lista2:
            if i == j:
                encontrado = True
                break

    if encontrado == True:
        return True
    else:
        return False

listaA = [1, 2, 3]
listaB = [4, 5, 6]

respuesta = superposicion(listaA, listaB)

print(respuesta)