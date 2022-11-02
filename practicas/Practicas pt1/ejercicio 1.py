"""
    1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
    (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def max(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        print("Error: no hay numero mayor.")

error = True
while error == True:
    try:
        numero1 = int(input("Ingresa numero1: "))
        numero2 = int(input("Ingresa numero2: "))
        
        resultado = max(numero1, numero2)

        print("El numero mayor es: {}".format(resultado))

        error = False
    except:
        print("Ha ocurrido un error, intentalo de nuevo.")
        error = True