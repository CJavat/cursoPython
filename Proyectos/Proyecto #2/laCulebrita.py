import turtle
import time
import random

#! CREACIÓN DE LA VARIABLE QUE LE DARÁ UN DELAY A LA SERPIENTE ANTES DE MOVERSE.
retraso = 0.1 

#! CREACIÓN DE VARIABLE PARA MARCADOR:
marcador = 0
marcadorAlto = 0

#! CREACIÓN Y CONFIGURACIÓN DE LA PANTALLA.
s = turtle.Screen()
s.setup(650, 650) # ASIGNARLE UN TAMAÑO A LA VENTANA.
s.bgcolor("gray")
s.title("PROYECTO #2 - SNAKE GAME")

#! CREACIÓN DE LA SERPIENTE.
serpiente = turtle.Turtle()
serpiente.speed(3)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = "stop"
serpiente.color("green")

#! CREACIÓN DE LA COMIDA.
comida = turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0, 100)
comida.speed(0)

#! CREACIÓN DE LA LISTA PARA EL CUERPO DE LA SERPIENTE.
cuerpo = []

#! CREACIÓN DEL TEXTO DEL PUNTAJE.
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0, -260)
texto.write("Marcador: 0\tMarcador mas alto: 0", align="center", font=("verdana", 20, "normal")) # ESCRIBIR EL PUNTAJE.

#! CREACIÓN DE FUNCIÓN PARA DECIRLE PARA DONDE SE VA A MOVER LA SERPIENTE.
def arriba():
    serpiente.direction = "up"

def abajo():
    serpiente.direction = "down"

def derecha():
    serpiente.direction = "right"

def izquierda():
    serpiente.direction = "left"

#! MOVIMIENTO DE LA SERPIENTE.
def movimiento():
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x - 20)

#! CREACIÓN DE MOVIMIENTO CON LAS TECLAS.
s.listen() # PONE A QUE ESCUCHÉ LA PANTALLA CUALQUIER EVENTO. (CUANDO ALGUNA TECLA SEA PRESIONADA)
# EVENTO A LA PANTALLA DE LA TECLA PRESIONADA.
#* SINTAXIS: SCREEN.onkeypress(función, "NOMBRE DE LA TECLA")
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(izquierda, "Left")
s.onkeypress(derecha, "Right")

#! CLICLO PARA QUE SIEMPRE SE REPITA.
while True:
    s.update() #* PARA QUE SE ESTÉ ACTUALIZANDO LA PANTALLA.
    
    #* CONFIGURACIÓN PARA QUE SE REPITA EL JUEGO CUANDO LA SERPIENTE COLISIONA EN ALGÚN BORDE DE LA PANTALLA.
    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = "stop"
        cuerpo.clear()
        
        marcador = 0
        texto.clear()
        texto.write("Marcador: {}\tMarcador mas alto: {}".format(marcador, marcadorAlto), align="center", font=("verdana", 20, "normal"))
    
    #* CONDICION PARA QUE CUANDO TOQUE LA COMIDA, CAMBIE DE POSICIÓN
    if serpiente.distance(comida) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x, y)
        
        #* CREACIÓN DE CADA BOLITA NUEVA DEL CUERPO DE LA SERPIENTE.
        nuevoCuerpo = turtle.Turtle()
        nuevoCuerpo.shape("square")
        nuevoCuerpo.color("green")
        nuevoCuerpo.penup()
        nuevoCuerpo.goto(0, 0)
        nuevoCuerpo.speed(0)
        cuerpo.append(nuevoCuerpo)
        
        marcador += 10
        if marcador > marcadorAlto:
            marcadorAlto = marcador
            texto.clear()
            texto.write("Marcador: {}\tMarcador mas alto: {}".format(marcador, marcadorAlto), align="center", font=("verdana", 20, "normal"))
        
    #* HACER QUE EL CUERPO SE AGREGUÉ A LA LISTA Y DESPUÉS SIGA A LA SERPIENTE.
    total = len(cuerpo)
    for index in range(total -1, 0, -1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x, y)
    
    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x, y)
            
    movimiento()
    
    #* CONFIGURACIÓN PARA QUE SE REPITA EL JUEGO CUANDO LA SERPIENTE COLISIONA CON SU CUERPO.
    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction = "stop"
            
            marcador = 0
            texto.clear()
            texto.write("Marcador: {}\tMarcador mas alto: {}".format(marcador, marcadorAlto), align="center", font=("verdana", 20, "normal"))
    
    time.sleep(retraso) # PARA DARLE UN RETRASO AL MOVIMIENTO.















turtle.done()