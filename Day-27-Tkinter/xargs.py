def add(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(**kwargs):
    for (key, value) in kwargs.items():
        print(f'{key} : {value}')


calculate(add=3, multiply=5, substract=6, divide=10)