import random
from colors import colors_list
from tim_turtle import tim, screen


def choose_random():
    return random.choice(colors_list)


def draw_lines(y_gap, limit=240):
    counter = 0
    continue_running = True
    while continue_running:
        y_pos = -260 + (y_gap*counter)
        counter += 1
        if y_pos > limit:
            continue_running = False
        tim.penup()
        tim.setpos(-310, y_pos)
        moved_steps = 0
        while moved_steps < 590:
            tim.dot(20, choose_random())
            tim.fd(61)
            tim.dot(20, choose_random())
            moved_steps += 61


draw_lines(58)

screen.exitonclick()
