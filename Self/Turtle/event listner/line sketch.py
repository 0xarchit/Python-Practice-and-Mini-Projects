import turtle as t

turt = t.Turtle()
turt.shape('turtle')
screen = t.Screen()

def move_forwards():
    turt.forward(10)

def move_backwards():
    turt.backward(10)

def turn_left():
    new_heading = turt.heading() + 10
    turt.setheading(new_heading)

def turn_right():
    new_heading = turt.heading() - 10
    turt.setheading(new_heading)

def clear():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()