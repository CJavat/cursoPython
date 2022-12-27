"""
    Escriba una función es_bisiesto() que determine si un año determinado es un año
    bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
"""
def es_bisiesto(año):
    if (año%400 == 0) or (año%4 ==0 and año%100 != 0):
        print("El año {} es bisiesto.".format(año))
    else:
        print("El año {} NO es bisiesto.".format(año))


añoDado = int(input("INTRODUCE UN AÑO: "))

es_bisiesto(añoDado)