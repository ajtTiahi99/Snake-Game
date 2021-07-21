from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0,310)
        self.write(f"Score: {self.score}",align='center',font=("Arial", 25, "normal"))
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=("Arial", 25, "normal"))

    def game_over(self):
        self.setposition(0,0)
        self.write(f"GAME OVER!",align='center', font=("Arial", 25, "normal"))
