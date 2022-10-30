"""
    Crear un programa que tenga dos funciones, 
    una que contenga el area de un cuadrado con argumentos de base y altura; 
    y la otra el area de un circulo con argumento de radio
"""
PI = 3.14

def areaCuadrado(lado):
    area = lado * lado
    return area

def areaCirculo(radio):
    area = PI * (radio ** 2)
    return area

ladoCuadrado = int(input("ESCRIBE EL LADO DEL CUADRADO: "))
radioCirculo = float(input("ESCRIBE EL RADIO DEL CIRCULO: "))

print("EL AREA DEL CUADRADO ES: ", areaCuadrado(ladoCuadrado))
print("EL AREA DEL CIRCULO: ", areaCirculo(radioCirculo))