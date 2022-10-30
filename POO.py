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
""" class FabricaTelefonos:
    # ATRIBUTOS
    marca = "Huawei"
    color = "Negro"
    ram = 32
    almacenamiento = 128

    # MÉTODOS
    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando musica") """

# DECLARAR VARIABLE TIPO CLASE
""" telefono = FabricaTelefonos()

# ACCEDER A LOS ATRIBUTOS DE LA CLASE
telefono.marca
telefono.color
telefono.ram
telefono.almacenamiento

#ACCEDER A LOS MÉTODOS DE LA CLASE
print(telefono.llamar("HOLA MUNDO"))
telefono.escucharMusica()

print(telefono.almacenamiento) """

# SELF E INIT
# SELF:
""" class FabricaTelefonos():
    marca = 'Samsung'

    def ElaborarHuawei(self):
        self.marca = "Huawei" # PARAMETRO SELF ES PARA ENGLOBAR LOS ATRIBUTOS.

telefono = FabricaTelefonos()
telefono.ElaborarHuawei()
print(telefono.marca) """

# INIT: CONSTRUCTOR DE UNA CLASE.
""" class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos('Huawei', 'Negro')

print(telefono.marca)
print(telefono.color) """

# METODOS ESPECIALES
""" class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("El objeto ", self.marca, " ha sido creado.")

    def __str__(self): # SIRVE PARA MOSTRAR UN MENSAJE.
        return "El objeto es: {}".format(self.marca)

    def __del__(self): # DECONSTRUCTOR. ELIMINA EL OBJETO DE LA MEMORIA.
        print("El objeto ", self.marca, " ha sido destruido.")

telefono = FabricaTelefonos('Huawei', 'Positivo')

print(telefono.marca)
print(telefono) """

# PROFUNDIZANDO EN POO.
""" # ** => SIGNIFICA QUE ES UN DICCIONARIO.
# *  => SIGNIFICA QUE ES UNA TUPLA.
class FabricaTelefonos():
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos('Huawei', "Negro", "Azul", "Rojo", m1 = 500, m2 = 1000)

print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)

# ATRIBUTOS TEMPORALES.
telefono.memoria = 512
print(telefono.memoria) """

# INTRODUCCION A LOS PILARES DE LA POO.
# ENCAPSULAMIENTO, HERENCIA Y POLIMORFISMO.

#! ENCAPSULAMIENTO: APLICAR SOBRE LOS ATRIBUTOS CIERTOS ALCANCES PARA QUE SOLO EN LA CLASE SE UTILICEN.
""" class A():
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0

    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador

a = A()
print("Objeto 1")
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)

print("Objeto 2")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador) # ESO ES ENCAPSULAMIENTO.
# HACE QUE NO PUEDAS ACCEDER A LOS ATRIBUTOS, SINO QUE DESDE LA CLASE. """

""" class A():
    def __init__(self, contador, cuenta):
        self._contador = contador # SOLO SE DECLARA CON UN _ LA VARIABLE PARA DECIRLE A OTROS PROGRAMADORES DEL ENCAPSULAMIENTO.
        self._cuenta = cuenta
"""

# METODO GET.
""" class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    # FORMA DE DECLARAR EL METODO GET.
    @property # CON ESTO ES PARA DECIRLE QUE PUEDA ACCEDER COMO ATRIBUTO Y NO COMO UN METODO.
    def cuenta(self):
        return self._cuenta

    @property # SE DEBE DE PONER ARRIBA DE CADA DECLARACION
    def contador(self):
        return self._contador

a = A()
print(a.cuenta) # FORMA CORRECTA DE LLAMAR CON EL METODO GET.
print(a.contador) # FORMA CORRECTA DE LLAMAR CON EL METODO GET. """

# METODO SET.
""" class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    # FORMA DE DECLARAR EL METODO GET.
    @property # CON ESTO ES PARA DECIRLE QUE PUEDA ACCEDER COMO ATRIBUTO Y NO COMO UN METODO.
    def cuenta(self):
        return self._cuenta

    @cuenta.setter # DECORADOR SETTER. FORMA DE DECLARARLO
    def cuenta(self, cuenta):
        self._cuenta = cuenta

    @property # SE DEBE DE PONER ARRIBA DE CADA DECLARACION
    def contador(self):
        return self._contador

    @contador.setter
    def contador(self, contador):
        self._contador = contador

a = A()
a.cuenta = 20 # FORMA DE ENTRAR AL METODO SET.
print(a.cuenta) # FORMA CORRECTA DE LLAMAR CON EL METODO GET.
a.contador = 1
print(a.contador) # FORMA CORRECTA DE LLAMAR CON EL METODO GET. """

#! HERENCIA: HEREDA ATRIBUTOS O METODOS DE LA CLASE PADRE A LA HIJA.
""" class Animales(): # CLASE PADRE.
    def habla(self):
        print("Yo soy un animal.")

    def descripcion(self):
        print("Yo soy un {}".format(self.animal))

class Perro(Animales): # CLASE HIJA.
    pass

class Abeja(Animales): # CLASE HIJA.
    def __init__(self, animal):
        self.animal = animal

animal = Animales()
animal.habla()

perro = Perro()
perro.habla()

abeja = Abeja("Abeja")
abeja.descripcion() """

# ERRORES CON LA HERENCIA.
""" class Animales(): # CLASE PADRE.
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animales): # CLASE PADRE.
    def __init__(self, nombre, sonido):
        super().__init__(nombre) # FORMAS PARA INICIALIZAR UNA VARIABLE YA HEREDADA.
        self.sonido = sonido

perro = Perro("Firulais", 'Guau')

print(perro.nombre)
print(perro.sonido) """

# HERENCIA MULTIPLE.
""" class A():
    def primera(self):
        return "Esta es la calse A."

class B():
    def segunda(self):
        return "Esta es la calse B."

class C(A, B): # FORMA DE DECLARAR UNA HERENCIA MULTIPLE.
    pass

c = C()

print(c.primera())
print(c.segunda()) """

#! POLIMORFISMO: MODIFICACION DE METODOS CUANDO SE HEREDAN DE OTRAS CLASE O CREAR OBJETOS QUE APUNTEN/USEN EL MISMO METODO PERO QUE EL OBJETO SEA DIFERENTE.
class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo no hablo")

class Pez(Animales):
    def hablar(self):
        print("YO TAMPOCO HABLO")

animal = Animales("Miau")
animal.hablar()

perro = Perro('GUAU')
perro.hablar()

pescado = Pez("GLUC")
pescado.hablar()












