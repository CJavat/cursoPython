"""
    En la siguiente lista, debes hacer un programa que muestre los valores al usuario, 
    a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

    [20, 50, "Curso", 'Python', 3.14]
"""

lista = [20, 50, "Curso", 'Python', 3.14]

print("Datos en la lista:\n", lista)

dato1 = input("Ingresa un dato: ")
dato2 = input("Ingresa otro dato: ")

lista.insert(0, dato1)
lista.insert(1, dato2)

print("Datos actualizados en la lista:\n", lista)