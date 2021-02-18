import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^', '<', '>', '/', '@', '¿']


def random_password_generator():
    password = ''
    while len(password) < 21:
        random_list = random.randint(1, 3)
        list_to_choose_from = letters if random_list == 1 else numbers if random_list == 2 else symbols
        random_letter = random.choice(list_to_choose_from)
        password += random_letter
    return password
