"""
    Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, 
    conociendo las notas de: tres prácticas, el examen parcial y el examen final.

    Considere:

    PP = ( P1 + P2 +P3 ) / 3 
    PROM = ( PP + 2*EP + 3*EF ) / 6

    Donde: P1, P2, P3 : Practicas

    PP: promedio de práctica

    PROM: promedio

    EP: examen parcial

    EF: examen final
"""
P1 = float(input("Escribe la calificacion de la primera practica"))
P2 = float(input("Escribe la calificacion de la segunda practica"))
P3 = float(input("Escribe la calificacion de la tercera practica"))
EP = float(input("Escribe la calificacion del Examen Parcial"))
EF = float(input("Escribe la calificacion del Examen Final"))

PP = ( P1 + P2 +P3 ) / 3 
PROM = ( PP + 2*EP + 3*EF ) / 6

print("El promedio final es: ", PROM)