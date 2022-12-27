"""
    Definir una lista con un conjunto de nombres, imprimir la cantidad que comienzan con la letra a.
    También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

nombres = ["carlos", "daniel", "oliver", "issac"]
contador = 0

inicial = input("Escribe la inicial con la que quieres buscar en la lista de nombres: ")

for i in nombres:
    if i.startswith(inicial):
        contador += 1

print("Total de personas que comienzan con la letra '{}' son: {}".format(inicial, contador))