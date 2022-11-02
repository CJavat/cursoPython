"""
    10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
    Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
    ****
    *********
    *******
"""
def procedimiento(lista):
    for i in lista:
        sumarCaracteres = ""
        for j in range(i):
            sumarCaracteres += "*"
        print(sumarCaracteres)

lista = [4, 9, 7]

procedimiento(lista)