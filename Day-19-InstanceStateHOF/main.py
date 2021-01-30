from tim_turtle import tim, screen


def move_forward():
    tim.fd(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
