from turtle import Screen
import time

from Snake_Game.snake_class import Snake
from Snake_Game.food import Food
from Snake_Game.score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
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

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()

