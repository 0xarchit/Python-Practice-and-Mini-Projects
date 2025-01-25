import turtle as t
import random
from tkinter import messagebox

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bat = screen.textinput(title="Make your bet", prompt="which turtle win? enter your color: ")

all_turtle = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_pos = [-70, -40, -10, 20, 50, 80]
for turt_index in range(0, 6):
    turt = t.Turtle(shape="turtle")
    turt.color(colors[turt_index])
    turt.penup()
    turt.goto(x = -230, y = y_pos[turt_index])
    all_turtle.append(turt)

if user_bat:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()
            is_race_on = False
            if win_color == user_bat:
                messagebox.showinfo("You win!", f"You Win, your {win_color} turtle win!")
            else:
                messagebox.showinfo("You lose!", f"You Lose, the {win_color} turtle win!")
                break
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()