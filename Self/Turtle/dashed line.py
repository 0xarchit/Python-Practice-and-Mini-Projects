import turtle as t

turt = t.Turtle()
turt.shape('turtle')

for _ in range(15):
    turt.forward(10)
    turt.penup()
    turt.forward(10)
    turt.pendown()

screen = t.Screen()
screen.exitonclick()