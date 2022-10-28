# INTRODUCCIÓN A LA POO (Programación ORIENTADA a Objetos)
""" 
    CLASES --> MOLDE DE GALLETAS
    OBJETOS --> LAS GALLETAS
"""

# DECLARACIÓN DE UNA CLASE. SINTAXIS

""" class FabricaTelefonos():
    pass

print(type(FabricaTelefonos))

celular1 = FabricaTelefonos()
celular2 = FabricaTelefonos()

print(type(celular1))
print(type(celular2)) """

# ATRIBUTOS Y MÉTODOS
class FabricaTelefonos:
    # ATRIBUTOS
    marca = "Huawei"
    color = "Negro"
    ram = 32
    almacenamiento = 128

    # MÉTODOS
    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando musica")

# DECLARAR VARIABLE TIPO CLASE
telefono = FabricaTelefonos()

# ACCEDER A LOS ATRIBUTOS DE LA CLASE
telefono.marca
telefono.color
telefono.ram
telefono.almacenamiento

#ACCEDER A LOS MÉTODOS DE LA CLASE
print(telefono.llamar("HOLA MUNDO"))
telefono.escucharMusica()

print(telefono.almacenamiento)

# SELF E INIT
















