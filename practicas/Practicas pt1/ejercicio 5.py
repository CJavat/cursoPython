"""
    5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
    Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def sum(lista):
    suma = 0
    for i in lista:
        print(i, "\n")
        suma += i
    return suma

def multip(lista):
    multiplicacion = 1
    for j in lista:
        multiplicacion *= j
    return multiplicacion

lista = []

seguirIngresandoDatos = True
while seguirIngresandoDatos == True:
    try:
        dato = int(input("INGRESA UN NUMERO: "))
        lista.append(dato)

        respuesta = input("Quieres seguir ingresando datos?, responde si o no\n")
        if respuesta.lower() == "si":
            seguirIngresandoDatos = True
        elif respuesta.lower() == "no":
            seguirIngresandoDatos = False
    except:
        print("Error al introducir el dato. SOLO SE ACEPTAN NUMEROS.")
        seguirIngresandoDatos = True

resultadoSuma = sum(lista)
resultadoMultiplicacion = multip(lista)

print("El resultado de la suma es: {}\nEl resultado multiplicacion es: {}".format(resultadoSuma, resultadoMultiplicacion))