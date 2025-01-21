import turtle as t

turt = t.Turtle()
turt.shape('turtle')
turt.color('red')

for _ in range(4):
    turt.forward(100)
    turt.right(90)

screen = t.Screen()
screen.exitonclick()