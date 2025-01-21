import turtle as t
import random

turt = t.Turtle()
turt.shape('turtle')
screen = t.Screen()

def move_forwards():
    turt.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()