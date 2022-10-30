"""
    Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
    luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 
    Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
    Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno
"""

class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

    def mostrar(self):
        print("La moto es color {} y tiene {} llantas, su precio es de: {} \n".format(self.color, self.llantas, self.precio))


class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

    def mostrar(self):
        print("El carro es color {} y tiene {} llantas, su precio es de: {} \n".format(self.color, self.llantas, self.precio))

moto = Moto(2, 'Negro', '$15000')
carro = Carro(4, 'Blanco', '$30000')

moto.mostrar()
carro.mostrar()
