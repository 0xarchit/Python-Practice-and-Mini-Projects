import turtle as t
import random

turt = t.Turtle()
turt.hideturtle()
turt.speed("fastest")
t.colormode(255)

turt.penup()
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


turt.setheading(200)
turt.forward(300)
turt.setheading(0)
num_of_dots = 100

for cnt in range(1, num_of_dots + 1):
    turt.dot(20, random.choice(color_list))
    turt.forward(50)
    if cnt % 10 == 0:
        turt.setheading(90)
        turt.forward(50)
        turt.setheading(180)
        turt.forward(500)
        turt.setheading(0)


screen = t.Screen()
screen.exitonclick()