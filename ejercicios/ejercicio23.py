"""
    Crear un programa que tenga una lista, 
    luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. 
    Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas
"""

lista = []
listaPar = []
listaImpar = []

def listaAdd():
    numeros = int(input("ESCRIBE EL NUMERO QUE QUIERES AGREGAR A LA LISTA: "))
    lista.append(numeros)

agregarNumeros = int(input("INGRESA CUANTOS NUMEROS QUIERES AGREGAR: "))

i = 1
while i <= agregarNumeros:
    listaAdd()
    i += 1

def ordenarNumeros():
    for j in lista:
        if(j%2 == 0):
            listaPar.append(j)
        else:
            listaImpar.append(j)
    listaPar.sort()
    listaImpar.sort()
ordenarNumeros()

print("La lista original es: ", lista, "\n")
print("La lista con los numeros pares: ", listaPar, "\n")
print("La lista con los numeros impares: ", listaImpar, "\n")













