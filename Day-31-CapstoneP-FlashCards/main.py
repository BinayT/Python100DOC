from tkinter import *
import random
import csv
from datetime import datetime
from tkinter import messagebox as mb
BACKGROUND_COLOR = "#B1DDC6"
TO_LEARN = []
KNOWS = []
CARD_PATH = 'images/card_back.png'
CURRENT_LANGUAGE = 'Language'
CURRENT_WORD = 'Word'

with open("data/french_words.csv", "r") as f:
    reader = csv.DictReader(f)
    current_word = list(reader)
random_word = None


def choose_word():
    global random_word
    random_word = random.choice(current_word)


def show_english():
    global CURRENT_WORD, CARD_PATH, CURRENT_LANGUAGE

    CURRENT_WORD = random_word['English']
    CARD_PATH = 'images/card_back.png'
    CURRENT_LANGUAGE = 'English'

    logo_img.config(file=CARD_PATH)
    canvas.itemconfig(card, image=logo_img)
    canvas.itemconfig(language, text=CURRENT_LANGUAGE)
    canvas.itemconfig(word, text=CURRENT_WORD)


def show_french():
    global CURRENT_WORD, CARD_PATH, CURRENT_LANGUAGE
    choose_word()
    CURRENT_WORD = random_word['French']
    CARD_PATH = 'images/card_front.png'
    CURRENT_LANGUAGE = 'French'

    logo_img.config(file=CARD_PATH)
    canvas.itemconfig(card, image=logo_img)
    canvas.itemconfig(language, text=CURRENT_LANGUAGE)
    canvas.itemconfig(word, text=CURRENT_WORD)

    window.after(3000, show_english)


def user_know():
    show_french()
    KNOWS.append({random_word['English']: random_word['French']})


def user_dont_know():
    show_french()
    TO_LEARN.append({random_word['English']: random_word['French']})


def exit_game():
    if mb.askyesno('Quit Game', 'You sure want to quit?'):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        with open(f'{len(TO_LEARN)+len(KNOWS)}-{len(TO_LEARN)}tolearn-{len(KNOWS)}correct.txt', mode="a+") as file:
            file.write(f'\ntime:{current_time}\nCorrect Ans:\n{KNOWS}\nTo Learn:\n{TO_LEARN}')
            # file.write("YOO")
        logo_img.config(file='')
        canvas.itemconfig(card, image='')
        canvas.itemconfig(language, text='')
        canvas.itemconfig(word, text='')


window = Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)

logo_img = PhotoImage(file=CARD_PATH)
card = canvas.create_image(400, 263, image=logo_img)
language = canvas.create_text(400, 150, text=CURRENT_LANGUAGE, font=("Arial", 40, 'italic'))
word = canvas.create_text(400, 263, text=CURRENT_WORD, font=("Arial", 40, 'italic'))
canvas.grid(column=0, row=0, columnspan=3)

show_french()
wrong_image = PhotoImage(file='images/wrong.png')
button_wrong = Button(image=wrong_image, highlightthickness=0, command=user_know)
button_wrong.grid(column=0, row=1)

exit_image = PhotoImage(file='images/exit.png')
button_exit = Button(image=exit_image, highlightthickness=0, command=exit_game)
button_exit.grid(column=1, row=1)

right_image = PhotoImage(file='images/right.png')
button_right = Button(image=right_image, highlightthickness=0, command=user_dont_know)
button_right.grid(column=2, row=1)

window.mainloop()