"""
    Crear un programa que permita al usuario elegir un candidato por el cual votar. 

    Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. 
    Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
    Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

    Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula
"""
candidatoA = "rojo"
candidatoB = "verde"
candidatoC = "azul"

voto = input("Escribe la letra por el candidato que quieres votar: ")

if voto.lower() == 'a':
    print("Usted ha votado por el partido ", candidatoA)
elif voto.lower() == 'b':
    print("Usted ha votado por el partido ", candidatoB)
elif voto.lower() == 'c':
    print("Usted ha votado por el partido", candidatoC)
else:
    print("Opcion erronea")