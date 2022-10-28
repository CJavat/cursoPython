"""
    Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
    La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
    Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""

def factura(cantidad, iva):
    if iva == 0:
        iva = 1.21
    elif iva < 0:
        print("ERROR - NO SE PUEDE APLICAR ESE IVA")
    else:
        iva /= 100
        iva += 1
    resultado = cantidad * iva
    return resultado

cantidadUser = int(input("INTRODUCE LA CANTIDAD: "))
ivaUser = int(input("INTRODUCE EL PORCENTAJE DE IVA A AGREGAR AL PRODUCTO: "))

print(factura(cantidadUser, ivaUser))