"""
    Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. 
    Definir los métodos para inicializar sus atributos, 
    imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""
class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimirlos(self):
        print("ALUMNO: {} Y SU NOTA ES: {}".format(self.nombre, self.nota))

        if(self.nota >= 60):
            print("\nHAS APROBADO.")
        else:
            print("\nNO APROBADO.")

estudiante = Estudiante("Daniel", 60)
estudiante2 = Estudiante("Carlos", 55)

estudiante.imprimirlos()
estudiante2.imprimirlos()