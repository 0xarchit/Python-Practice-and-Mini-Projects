import turtle as t
import random

turt = t.Turtle()
turt.shape('turtle')


def draw(num_sides):
    for i in range(num_sides):
        angle = 360/num_sides
        turt.color("red")
        turt.forward(100)
        turt.right(angle)

for i in range(3,12):
    draw(i)







screen = t.Screen()
screen.exitonclick()