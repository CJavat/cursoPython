# INTRODUCCIÓN A LAS LISTAS.

lista = ['python', 120, 'nombre', 4.14, 6.28, 3, 4, 5, "adss", "qwerty"] # Declaración de una lista

print(type(lista))
print(lista[2])
print(len(lista))

lista[0] = "PYTHON"

print(lista[0
])

# DEBANADO DE LISTAS.

print(lista[5])
print(lista[0 : 5])
print(lista[ : 5])
print(lista[0 : ])
print(lista[-5])
print(lista[-5 : ])
print(lista[ : -1])

# MÉTODOS DE LISTAS.

print(lista)
lista.append("hola mundo") # AGREGA ELEMENTO AL FINAL DE LA LISTA.
lista.pop() # ELIMINA ELEMENTO AL FINAL DE LA LSITA.
lista.insert(2, "Elemento en medio") # AGREGAR ELEMENTO EN EL INDICE QUE QUEREMOS.
lista.remove("Elemento en medio") # ELIMINA ELEMENTO QUE LE INDICAMOS.
lista.count("nombre") # RETORNA EL VALOR DE CUANTOS ELEMENTOS HAY CON ESE NOMBRE.
lista.index(4.14) # RETORNA EL INDICE EN EL QUE ESTÁ EL PRIMER VALOR QUE LE INIDICAMOS.
# lista.sort() # ORDENA ELEMENTO ASCENDENTE.
# lista.reverse # ORDENA ELEMENTO DESCENDENTE.

print(lista)
print(lista.count("nombre"))
print(lista.index(4.14))

# LLENAR UNA LISTA VACÍA.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

lista = []
edad = int(input("Ingresa tu edad: "))
lista.append(edad)
print(lista)