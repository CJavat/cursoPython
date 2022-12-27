"""
    Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, 
    cuantas letras "e" tiene y así hasta completar todas las vocales.
    Se puede hacer que el usuario sea quien elija la palabra.
"""
def contar_vocales(palabra):
    contador = 0
    
    contadorA = 0
    contadorE = 0
    contadorI = 0
    contadorO = 0
    contadorU = 0
    
    while contador < len(palabra):
        if palabra[contador].lower() == 'a':
            contadorA += 1
        elif palabra[contador].lower() == 'e':
            contadorE += 1
        elif palabra[contador].lower() == 'i':
            contadorI += 1
        elif palabra[contador].lower() == 'o':
            contadorO += 1
        elif palabra[contador].lower() == 'u':
            contadorU += 1
            
        contador += 1
    return contadorA, contadorE, contadorI, contadorO, contadorU

vocales = ('A', 'E', 'I', 'O', 'U')
palabraIngresada = input("Ingresa una palabra para contar las vocales: ")
vocalesContadas = contar_vocales(palabraIngresada)

cont = 0
for j in vocalesContadas:
    print("El total de vocal '{}' es: {}".format(vocales[cont], j))
    cont += 1