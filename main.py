from turtle import Turtle, Screen
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


dashedLine()















screen = Screen()
screen.exitonclick()