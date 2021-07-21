from turtle import Turtle

SET_POSITIONS = [(0, 0), (- 20, 0), (- 40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def add_segment(self,pos):
        new_turtle = Turtle('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.setpos(pos)
        self.turtles.append(new_turtle)

    def create_snake(self):
        for position in SET_POSITIONS:
            self.add_segment(position)

    def move(self):
        for turt_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turt_num - 1].xcor()
            new_y = self.turtles[turt_num - 1].ycor()
            self.turtles[turt_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
