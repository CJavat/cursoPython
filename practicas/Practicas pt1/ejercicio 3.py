"""
    3 - Definir una función que calcule la longitud de una lista o una cadena dada. 
    (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def calcularLongitud(lista):
    print(lista)
    longitud = 0
    for i in lista:
        longitud += 1
    
    return  longitud

lista = []

terminarLista = False
while terminarLista == False:
    dato = input("Ingrese un dato para agregarlo a la lista: ")
    lista.append(dato)

    respuesta = input("Quieres seguir agregando datos a la lista?, escribe: si o no\n")
    if respuesta.lower() == "si":
        terminarLista = False
    elif respuesta.lower() == "no":
        terminarLista = True
    else:
        print("Se ha producido un error en la respuesta dada.")

long = calcularLongitud(lista)

print("La longitud de una lista: {}".format(long))