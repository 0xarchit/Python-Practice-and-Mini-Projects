from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align="center", font=("Courier", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))
        self.goto(0,-30)
        self.write("Click anywhere on screen to Close", align="center", font=("Arial", 14, "normal"))
