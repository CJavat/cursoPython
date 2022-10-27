"""
    Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, 
    sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, 
    y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>
”"""
from math import sqrt



x1 = 0
x2 = 0

A = int(input("Escribe el valor de A: "))
B = int(input("Escribe el valor de B: "))
C = int(input("Escribe el valor de C: "))

if((B**2)-(4*A*C)) < 0:
    print("No se pueden sacar raiz a los numeros negativos")
else:
    x1 = (-B + sqrt((B**2)-(4*A*C))) / (2*A)
    x2 = (-B - sqrt((B**2)-(4*A*C))) / (2*A)
    print("La solución es: \n x1 = ", x1, "\nx2 = ", x2)

