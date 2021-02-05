from turtle import Screen
import time

from Snake_Game.snake_class import Snake
from Snake_Game.food import Food
from Snake_Game.score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.title('Snake Game')
screen.tracer(0)
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score += 1
        food.refresh()
        scoreboard.increase_score(score)
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # If head collides on any segment of the tail
        # trigger game over
    for snake_part in snake.snakes[1:]:
        if snake.head.distance(snake_part) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()

