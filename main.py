from turtle import Turtle, Screen
import random

brush = Turtle()
brush.shape("arrow")
brush.pencolor("#b342f5")
brush.pensize(3)
brush.speed(5)

random_direction = [90, 180, 270, 360]

def makeASquare():
    for i in range(4):
        brush.forward(100)
        brush.right(90)

def dashedLine():
    for i in range(50):
        brush.forward(5)
        brush.penup()
        brush.forward(5)
        brush.pendown()

def setRandomColour():
    red = random.random()
    green = random.random()
    blue = random.random()
    brush.pencolor(red, green, blue)

def makeMultipleShapes():
    side = 3
    while side <= 8:
        setRandomColour()
        for i in range(side):
            brush.forward(50)
            brush.right(360/side)
        side += 1

def randomWalk():
    for i in range(100):
        angle = int(random.choice(random_direction))
        brush.right(angle)
        brush.fd(30)
        setRandomColour()

randomWalk()










screen = Screen()
screen.exitonclick()