"""
    Crear una funcion que pida dos numeros. 
    Si el primero es mayor al segundo, el programa debe retornar el valor 1; 
    si el segundo es mayor al primero, debe retornar -1; 
    si ambos son iguales, debe retornar 0
"""

def pedirNumeros():
    numero1 = int(input("INTRODUCE EL VALOR DEL NUMERO 1: "))
    numero2 = int(input("INTRODUCE EL VALOR DEL NUMERO 2: "))

    if numero1 > numero2:
        return 1
    elif numero1 < numero2:
        return -1
    elif numero1 == numero2:
        return 0
    else:
        print("ERROR")

print(pedirNumeros())