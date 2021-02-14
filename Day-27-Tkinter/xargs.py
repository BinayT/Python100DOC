def add(*args):
    total = 0
    for num in args:
        total += num
    return total


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(**kwargs):
    for (key, value) in kwargs.items():
        print(f'{key} : {value}')


# calculate(add=3, multiply=5, subtract=6, divide=10)

class Car:
    def __init__(self, **kw):
        self.model = kw.get('model')
        self.year = kw.get('year')
        self.mileage = kw.get('model')

    def details_car(self):
        print(f"Your car is of model {self.model} of year {self.year} and it's mileage is of {self.mileage}km/l.")


my_car = Car(model="Toyota",  mileage=12)

my_car.details_car()