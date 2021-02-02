from turtle import Turtle, Screen
from Snake_Game.snake_class import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

turtles = []
for x in range(3):
    turtles.append(Snake(x_pos=0-(x*20), y_pos=0))

print(turtles)
screen.exitonclick()
