"""
    Escribir un pequeño programa donde:
    - Se ingresa el año en curso. (LISTO)
    - Se ingresa el nombre y el año de nacimiento de tres personas. (LSITO)
    - Se calcula cuántos años cumplirán durante el año en curso. ()
    - Se imprime en pantalla. ()
"""

anioEnCurso = int(input("Ingresa el año en curso: "))

contador = 0
infoPersonas = {}
calculandoAnios = {}
nombresDePersonas = []

while contador < 3:
    nombre = input("Ingresa tu nombre: ")
    anioDeNacimiento = int(input("Ingresa tu año de nacimiento: "))
    
    nombresDePersonas.append(nombre)
    
    infoPersonas.setdefault(nombre, anioDeNacimiento)
    contador += 1

contador2 = 0
while contador2 < 3:
    anioDeNacido = infoPersonas.get(nombresDePersonas[contador2])
    aniosCalculados = anioEnCurso - anioDeNacido
    
    calculandoAnios.setdefault(nombresDePersonas[contador2], aniosCalculados)
    contador2 += 1

for nombre in nombresDePersonas:
    print("{} cumple {} años en el {}".format(nombre.capitalize(), calculandoAnios.get(nombre), anioEnCurso))