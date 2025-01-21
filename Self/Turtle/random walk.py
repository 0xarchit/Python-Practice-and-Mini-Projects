import turtle as t
import random

turt = t.Turtle()
turt.shape('turtle')

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
turt.pensize(15)
turt.speed("fastest")

for _ in range(200):
    turt.color(random.choice(colours))
    turt.forward(30)
    turt.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()