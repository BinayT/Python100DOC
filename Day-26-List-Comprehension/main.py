from random import randint
list_1_to_3 = [1, 2, 3]
list_2_to_4 = [item+1 for item in list_1_to_3]

name = "Binay"
name_as_list = [char for char in name]

numbers_in_range = [num for num in range(1, 5)]
numbers_in_range_doubled = [number for number in numbers_in_range if number % 2 == 0]

names = ["Alex", "marTa", "JUaN", "BiNaY", "Pedro"]
names_in_upper = [name.upper() for name in names if len(name) < 5]

names_rand_score = {value : randint(0, 100) for value in names}
