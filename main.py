from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.bgcolor('black')
screen.tracer(8)

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or\
            snake.head.ycor() > 340 or snake.head.ycor() < -340:
        score.game_over()
        game_over = True

    for snake_body in snake.turtles[1:]:
        if snake.head.distance(snake_body) < 10:
            game_over = True
            score.game_over()

screen.exitonclick()
