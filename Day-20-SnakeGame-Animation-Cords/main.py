from turtle import Turtle, Screen
from Snake_Game.snake_class import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

snakes = []
for x in range(3):
    snakes.append(Snake(x_pos=0 - (x * 20), y_pos=0))

game_is_on = True
while game_is_on:
    for snake in snakes:
        snake.turtle.forward(20)
        if snake.turtle.pos() >= (270, 0):
            game_is_on = False

screen.exitonclick()
