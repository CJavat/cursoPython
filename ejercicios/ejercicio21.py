"""
    Imprimir por pantalla los numeros del 1 al 10, 
    luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras.
"""

for i in range(1, 11):
    print(i)

rangoInicial = int(input("Introduce el numero inicial del rango"))
rangoFinal = int(input("Introduce el numero final del rango"))

for j in range(rangoInicial, rangoFinal+1):
    print(j)