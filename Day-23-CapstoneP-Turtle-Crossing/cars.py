from turtle import Turtle
from random import randrange, randint
import time
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SHAPE = 'square'


class Cars:
    def __init__(self):
        super().__init__()
        self.cars = []

    def random_color(self):
        c1 = randint(0, 255)
        c2 = randint(0, 255)
        c3 = randint(0, 255)
        color = (c1, c2, c3)
        return color

    def make_random_cars(self):
        if randint(1, 7) % 2 != 0:
            random_y = randrange(-240, 240)
            car = Turtle()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.shape(CAR_SHAPE)
            car.color(self.random_color())
            car.goto(300, random_y)
            car.setheading(180)
            self.cars.append(car)

    def delete_car(self):
        for car in self.cars:
            if car.xcor() < -300:
                self.cars.remove(car)

    def move_car(self, score):
        print(len(self.cars))
        for car in self.cars:
            car.fd(5 + score*5)
            if car.xcor() < -325:
                self.cars.remove(car)
                del car
        time.sleep(0.2)
        self.make_random_cars()



