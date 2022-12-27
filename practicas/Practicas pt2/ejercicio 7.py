"""
    Definir una tupla con 10 edades de personas.
    Imprimir la cantidad de personas con edades superiores a 20.
    Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""
edadesDePersonas = (29, 20, 23, 23, 24, 26, 13, 5, 88, 50)

mayoresDe20 = ""

for i in edadesDePersonas:
    if i > 20:
        mayoresDe20 += str(i)
        mayoresDe20 += ", "
        
print("Las edades mayores a 20 son: {}".format(mayoresDe20))