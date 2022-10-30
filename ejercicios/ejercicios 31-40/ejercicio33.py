"""
    Crear un programa con tres clases:
    - Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). 
    - Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
    - Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
    El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.
"""

class Universidad():
    def __init__(self, nombreUniversidad):
        self.nombreUniversidad = nombreUniversidad

class Carrera():
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, nombreUniversidad, especialidad, nombre, edad):
        Universidad.__init__(self, nombreUniversidad) # HERENCIA DOBLE PARA OBTENER SUS ATRIBUTOS...
        Carrera.__init__(self, especialidad)          # ES LA FORMA DE HACERLO.

        self.nombre = nombre
        self.edad = edad

    def mostrarDatos(self):
        print("El estudiante {} con la edad de {} años estudia {} en la universidad: {}".format(self.nombre, self.edad, self.especialidad, self.nombreUniversidad))

persona = Estudiante('UDG', 'Programacion', 'Daniel', 23)

persona.mostrarDatos()