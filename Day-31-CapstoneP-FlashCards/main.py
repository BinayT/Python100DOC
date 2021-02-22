from tkinter import *
from tkinter import messagebox as mb
from time import sleep
import pandas
BACKGROUND_COLOR = "#B1DDC6"
SCORE = 0

window = Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

logo = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
logo_img = PhotoImage(file='images/card_back.png')
logo.create_image(400, 263, image=logo_img)
logo.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file='images/wrong.png')
button_wrong = Button(image=wrong_image, highlightthickness=0)
button_wrong.grid(column=0, row=1)

right_image = PhotoImage(file='images/right.png')
button_right = Button(image=right_image, highlightthickness=0)
button_right.grid(column=1, row=1)

window.mainloop()