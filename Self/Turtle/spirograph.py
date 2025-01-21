import turtle as t
import random

turt = t.Turtle()
t.colormode(255)
turt.shape('turtle')

turt.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw(size_of_gap):
    for _ in range(360//size_of_gap):
        turt.color(random_color())
        turt.circle(100)
        turt.setheading(turt.heading() + size_of_gap)

draw(5)













screen = t.Screen()
screen.exitonclick()