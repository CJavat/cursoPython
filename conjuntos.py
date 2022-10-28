# INTRODUCCIÓN A LOS CONJUNTOS.

# FORMAS DE DECLARAR LOS CONJUNTOS.
# conjunto = {1, 2, 3, 4, 5}
# conjunto = set[(1, 2, 3, 4, 5)]
# conjunto = set((1, 2, 3, 4, 5))

# print(type(conjunto))

# MÉTODOS DE LOS CONJUNTOS.

conjunto = {1, 2, 3, 4, 5}
lista = [1, 1, 2, 3, 4, 4]

# LA DIFERENCIA ES QUE LAS LISTAS SI MUESTRAN LOS DATOS REPETIDOS Y LOS CONJUNTOS NO.
print(lista)
print(conjunto)

conjunto.add(20) # AGREGA UN ELEMENTO AL FINAL DEL CONJUNTO.
conjunto.remove(20) # ELIMINA EL ELEMENTO INDICADO.
conjunto.discard(1) # ELIMINA EL ELEMENTO INDICADO.
conjunto.pop() # ELIMINA UN ELEMENTO AL AZAR.
conjunto.update([7, 8, 9]) # LE SUMA EL NUEVO CONJUNTO AL VIEJO.
conjunto.clear() # ELIMINA TODOS LOS DATOS.

print(conjunto)