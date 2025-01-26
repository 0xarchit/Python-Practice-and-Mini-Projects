import turtle as t
import random
from tkinter import messagebox

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

start_pos = [(0,0), (-20,0), (-40,0)]
for pos in start_pos:
    new_segment = t.Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(pos)






# messagebox.showinfo("You lose!", f"You Lose, the {win_color} turtle win!")
screen.exitonclick()