from tkinter import *
import random
import csv
BACKGROUND_COLOR = "#B1DDC6"
SCORE = 0
NEXT = False
CARD_PATH = 'images/card_front.png' if NEXT else 'images/card_back.png'
CURRENT_LANGUAGE = 'English' if NEXT else 'French'
CURRENT_WORD = None

with open("data/french_words.csv", "r") as f:
    reader = csv.DictReader(f)
    current_word = list(reader)


def show_english():
    global CURRENT_WORD, NEXT
    NEXT = not NEXT
    random_word = random.choice(current_word)
    CURRENT_WORD = random_word['English'] if NEXT else random_word['French']
    print(CURRENT_WORD)
    logo_img.config(file=CARD_PATH)
    canvas.itemconfig(card, image=logo_img)
    canvas.itemconfig(language, text=CURRENT_LANGUAGE)
    canvas.itemconfig(word, text=CURRENT_WORD)

    if NEXT:
        window.after(3000, show_english)


window = Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)

logo_img = PhotoImage(file=CARD_PATH)
card = canvas.create_image(400, 263, image=logo_img)
language = canvas.create_text(400, 150, text=CURRENT_LANGUAGE, font=("Arial", 40, 'italic'))
word = canvas.create_text(400, 263, text=CURRENT_WORD, font=("Arial", 40, 'italic'))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file='images/wrong.png')
button_wrong = Button(image=wrong_image, highlightthickness=0, command=show_english)
button_wrong.grid(column=0, row=1)

right_image = PhotoImage(file='images/right.png')
button_right = Button(image=right_image, highlightthickness=0, command=show_english)
button_right.grid(column=1, row=1)

window.mainloop()