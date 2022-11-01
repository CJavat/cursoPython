# INTRODUCCIÓN A TURTLE.
from time import sleep
import turtle

pantalla = turtle.Screen() # ASIGNAR LA PANTALLA GRÁFICA.
punto = turtle.Turtle() # ASIGNAR LA PUNTO QUE VA A TRAZAR TODO.

#! COMANDOS BÁSICOS PARA MOVER LA TORTUGA.
""" punto.backward(100)
punto.right(90)
punto.forward(100)
punto.left(90)
punto.forward(100)
punto.left(90)
punto.forward(100) """

""" punto.fd(100)
punto.rt(90)
punto.bk(100)
punto.lt(90) """


#! MOVIMIENTO DE LA TORTUGA EN EL LIENZO.
# TRIANGULO.
""" punto.goto(100, 100)
punto.goto(-100, 100)
# punto.goto(0, 0)
punto.home()

# CUADRADO.
punto.forward(100)
punto.right(90)
punto.forward(100)
punto.right(90)
punto.forward(100)
punto.right(90)
punto.forward(100)
punto.right(90) """

#! COMANDOS ESPECIALES.
""" punto.speed(10) # ASIGNARLE VELOCIDAD A LA TORTUGA (VALORES DEL 1 - 10)

punto.circle(10) # TRAZAR UN CIRCULO CON EL DIAMETRO INDICADO.
punto.speed(10)

punto.circle(50)
punto.circle(100)

punto.speed(10)
punto.dot(25) # TRAZA UN CIRCULO PERO RELLENADO.

punto.hideturtle() # ESCONDE LA TORTUGA DE LA PANTALLA.
punto.speed(2)
punto.circle(150)

punto.showturtle() # MUESTRA DE NUEVO LA TORTUGA EN LA PANTALLA.
punto.circle(200)

# MUEVE LA TORTUGA EN LAS CORDENADAS X o Y
punto.setx(-150)
punto.sety(-150) """

#! PERSONALIZAR PANTALLA Y TORTUGA.
""" pantalla.bgcolor("black") # CAMBIAR EL COLOR DE FONDO DE LA PANTALLA.
pantalla.title("Proyecto 1") # CAMBIA EL NOMBRE DE LA VENTANA.

punto.color("white", "red") # CAMBIA DE COLOR COMPLETO DELA TORTUGA Y TINTA (COLORTINTA, COLORTORTUGA).
punto.pensize(5) # CAMBIA EL GROSOR DE LA LÍNEA PINTADA
punto.setx(100)
punto.fillcolor("red") # CAMBIA DE COLOR SOLO EL RELLENO.
punto.sety(100)
punto.pencolor("blue") # CAMBIA DE COLOR SOLO EL BORDE Y EL COLOR DE LA LÍNEA QUE PINTA LA TORTUGA.
punto.setx(150)
punto.shapesize(10, 5, 1) # CAMBIA LA FORMA DE LA TORTUGA. (ANCHO, LARGO, BORDE)
punto.shapesize(5, 10, 1)
punto.shapesize(3, 3, 3) """

#! OTROS ATRIBUTOS.
""" punto.begin_fill() # EMPIZA A LLENAR LAS FIGURAS
punto.circle(100)
punto.end_fill() # TERMINA DE LLENAR LA FIGURA TRAZADA.

punto.begin_fill()
punto.color("white", "white")
punto.circle(50)
punto.end_fill() """

# CAMBIAR LA FORMA DE LA TORTUGA.
punto.shape("turtle")
""" punto.shape("arrow")
punto.shape("circle")
punto.shape("square")
punto.shape("triangle")
punto.shape("classic") """

""" punto.penup() # LEVANTA EL LÁPIZ PARA QUE NO TRACE NADA CUANDO MUEVAS DE COORDENADA EL PUNTERO.
punto.forward(100)
punto.pendown() # BAJA EL LÁPIZ PARA QUE PUEDAS EMPEZAR A PINTAR DE NUEVO.
punto.forward(100)
punto.penup()
punto.forward(100)

punto.undo() # ES COMO UN CONTROL+Z LA TORTUGA SE REGRESA Y DESHACE LO QUE HABÍA HECHO LA ÚLTIMA VEZ. 
punto.clear() # SE LIMPIA/BORRA TODA LA PANTALLA PERO LA TORTUGA QUEDA EN EL MISMO LUGAR.
punto.reset() # REINICIA POR COMPLETO TODO EL PROGRAMA.

punto.forward(100)
punto.stamp() # DEJA UNA MARCA/SELLO EN LA PANTALLA.
punto.right(90)
punto.forward(100)
punto.stamp()
punto.right(90)
punto.forward(100)
punto.stamp()
punto.right(90)
punto.forward(100)
punto.stamp() """

#! AUTOMATIZADO DE PROCESOS.
""" punto.forward(100)
punto.right(90)
punto.forward(100)
punto.right(90)
punto.forward(100)
punto.right(90)
punto.forward(100) """

""" for i in range(4):
    punto.forward(100)
    punto.right(90) """

resultado = input("Quieres imprimir una figura?")
if resultado == "si":
    i = 100
    while i >= 10:
        punto.circle(i)
        i -= 10
else:
    print("oka")


pantalla.bye(sleep(2)) # CERRAR LA PANTALLA. Y CON SLEEP LE DIGO QUE SE ESPERE 5 SEGUNDOS ANTES DE CERRAR LA PANTALLA.





















turtle.done() # MANTENER LA PANTALLA ABIERTA.