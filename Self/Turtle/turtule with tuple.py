import turtle as t
import random

turt = t.Turtle()
t.colormode(255)
turt.shape('turtle')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return r, g, b

directions = [0, 90, 180, 270]
turt.pensize(15)
turt.speed("fastest")

for _ in range(200):
    turt.color(random_color())
    turt.forward(30)
    turt.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()