import turtle as t
import random
from tkinter import messagebox
import time
import snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = snake.Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()






messagebox.showinfo("Completed", "Completed")
screen.exitonclick()