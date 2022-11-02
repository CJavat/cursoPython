"""
    La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), 
    solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. 
    Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
"""

def max_in_list(lista):
    mayor = 0
    for i in lista:
        print("I: ", i)
        j=0
        while j < len(lista):
            print("J: ", lista[j])
            if i > lista[j] and i > mayor:
                mayor = i
            elif lista[j] > i and lista[j] > mayor:
                mayor = lista[j]
            """ else:
                mayor = mayor """

            print("I: ", i)
            print("J: ", lista[j])
            print("MAYOR: ", mayor, "\n")
            j += 1
    print("MAYOR: ", mayor)

lista = [11, 10, 19, 14]

max_in_list(lista)