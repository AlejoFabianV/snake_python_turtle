from turtle import *
import random, time

#crear y config screen
screen = Screen() #objeto de turtle
screen.title("Snake Game") #titulo en la pantalla
screen.setup(width=700, height=700) #dimensiones de pantalla
screen.tracer(0) #desactiva la animacion auto
screen.bgcolor("brown") #color de fondo, python turtle color chart

#limites de pantalla
borde = Turtle() #objeto turtle para dibujo
borde.speed(5) #velocidad de dibujo
borde.pensize(2) #establece el grosor de la linea
borde.penup() #levanta el cursor, no muestra el proceso de dibujo
borde.goto(-290, 290) #punto de inicio al dibujo
borde.pendown() #baja el cursor, para comenzar el dibujo
borde.color("black") #asigna color al borde

#dibujo de cuadrado
for l in range(4): #repetimos 4 veces para los lados del cuadrado
    borde.forward(580) #avanzamos 580 unidades 
    borde.right(90) #giro 90 grados a la derecha

borde.penup()
borde.hideturtle() #esconde el shape

#crear y config de comida
fruit = Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(random.randint(-270, 270), random.randint(-270, 270))

before_fruit = [] #varia el tamaño de la serpiente

# variables del juego
score = 0 #puntaje inicial
delay = 0.1 #velocidad del juego

#config score
scoring = Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write(f"Score:  {format(score)}", align="center", font=("Coureir", 24, "bold")) #escibre el puntaje actual

serpiente = Turtle()
serpiente.speed(1)
serpiente.shape("circle")
serpiente.color("green")
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direction = "stop"

#funcion de movimiento
def serpiente_go_up():
    if serpiente.direction != "down":
        serpiente.direction = "up"

def serpiente_go_down():
    if serpiente.direction != "up":
        serpiente.direction = "down"

def serpiente_go_left():
    if serpiente.direction != "right":
        serpiente.direction = "left"

def serpiente_go_right():
    if serpiente.direction != "left":
        serpiente.direction = "right"

def move():
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

game_over = False

#colisiones
def colision_borde():
    x, y = serpiente.xcor(), serpiente.ycor()
    return x > 270 or x < -270 or y > 270 or y < -270

#reinicio de juego hecho con AI
def reiniciar_juego():
    global score, delay, serpiente, fruit, before_fruit, scoring, game_over

    # Reinicia el puntaje
    score = 0
    delay = 0.1

    # Reinicia la serpiente y la fruta
    serpiente.goto(0, 0)
    serpiente.direction = "stop"
    fruit.goto(random.randint(-270, 270), random.randint(-270, 270))

    for segment in before_fruit:
        segment.goto(1000, 1000)
    before_fruit.clear()

    # Limpia el marcador
    scoring.clear()
    scoring.goto(0, 300)
    scoring.write(f"Score: {format(score)}", align="center", font=("Coureir", 24, "bold"))

    game_over = False

#mapeo de teclas
screen.listen()
screen.onkeypress(serpiente_go_up, "Up")
screen.onkeypress(serpiente_go_down, "Down")
screen.onkeypress(serpiente_go_right, "Right")
screen.onkeypress(serpiente_go_left, "Left")
screen.onkeypress(reiniciar_juego, "space") 
screen.onkeypress("enter") 

while True:
    screen.update()

    if not game_over:
        move()

        if serpiente.distance(fruit) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270) #inverti el valor y funciono, en lugar de 280, -280, es -280, 280
            fruit.goto(x, y)

            scoring.clear() #limpia inmediatamente el valor anterior
            score += 1
            scoring.write(f"Score: {format(score)}", align="center", font=("Coureir", 24, "bold")) #arreglado con f string

            delay -= 0.001

            new_fruit = Turtle()
            new_fruit.speed(0)
            new_fruit.shape("circle")
            new_fruit.color("green")
            new_fruit.penup()
            before_fruit.append(new_fruit)
        
        for i in range(len(before_fruit) -1, 0, -1):
            a = before_fruit[i - 1].xcor()
            b = before_fruit[i - 1].ycor()
            before_fruit[i].goto(a, b)

        if len(before_fruit) > 0:
            a = serpiente.xcor()
            b = serpiente.ycor()
            before_fruit[0].goto(a, b)
        
        if colision_borde():
            serpiente.direction = "stop"
            scoring.goto(0, 0)
            scoring.write(f"Game Over, presiona ´espacio´ para reinicir", align="center", font=("Coureir", 18, "bold"))
            game_over = True
        
    time.sleep(delay)

screen.mainloop()