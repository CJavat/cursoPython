"""
    Crear un programa que pida al usuario:
        una letra
        y si es vocal, muestre el mensaje "Es vocal". 
        Sino, decirle al usuario que no es vocal
"""

letra = input("Escribe una letra: ")

if letra.upper() == 'A' or letra.upper() == 'E' or letra.upper() == 'I' or letra.upper() == 'O' or letra.upper() == 'U':
    print("Escribiste una vocal")
else:
    print("NO escribiste una vocal")