"""
    Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""
def numeroFactorial(numero):
    if numero < 0:
        print("No se aceptan numeros negativos.")
    elif numero == 0:
        return 1
    else:
        factorial = 1
        while numero > 0:
            factorial *= numero
            numero -= 1
        return factorial

num = int(input("ESCRIBE EL NUMERO AL QUE LE QUIERAS SACAR SU FACTORIAL: "))

mostrarResultado = numeroFactorial(num)

print("El resultado del factorial es: ", mostrarResultado)