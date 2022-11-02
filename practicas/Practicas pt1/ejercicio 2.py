"""
    2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

def max_de_tres(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    else:
        print("NO HAY NUMERO MAYOR.")

error = True
while error == True:
    try:
        numero1 = int(input("Ingresa numero 1: "))
        numero2 = int(input("Ingresa numero 2: "))
        numero3 = int(input("Ingresa numero 3: "))
        
        resultado = max_de_tres(numero1, numero2, numero3)

        print("El numero mayor es: {}".format(resultado))

        error = False
    except:
        print("Ha ocurrido un error, intentalo de nuevo.")
        error = True

