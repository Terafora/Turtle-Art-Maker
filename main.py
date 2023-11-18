from turtle import Turtle, Screen
import random

brush = Turtle()
brush.shape("arrow")
brush.pencolor("#b342f5")

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

makeMultipleShapes()












screen = Screen()
screen.exitonclick()