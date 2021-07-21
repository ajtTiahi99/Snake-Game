from turtle import Turtle
import random

colors = ['red', 'blue', 'purple', 'yellow', 'green', 'pink', 'violet', 'maroon']

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.refresh()

    def refresh(self):
        self.color(random.choice(colors))
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
