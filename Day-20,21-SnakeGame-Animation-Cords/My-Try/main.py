from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from collision_detection import collision_wall, collision_body
import time

SCREEN_BG_COLOR = 'black'
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(SCREEN_BG_COLOR)
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_right, 'Right')
screen.onkey(snake.move_down, 'Down')

score = 0
game_running = True
while game_running:
    time.sleep(0.15)
    screen.update()
    snake.move()
    if snake.snake_head.distance(food) < 10:
        food.update_spot()
        snake.snake_body_update()
        score += 1
        scoreboard.update_score(score)

    if collision_wall(snake.snake_head) or collision_body(snake.snake_body):
        game_running = False
        scoreboard.game_over(score)


screen.exitonclick()
