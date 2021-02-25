from tkinter import *
import requests
kayne_quotes = None

tk = Tk()
tk.title("Kayne Quotes")
tk.config(padx=100, pady=100)

label = Label(text='', font=("Courier", 22, 'bold'))


def get_kayne_quotes():
    global kayne_quotes
    kayne_quotes = requests.get("https://api.kanye.rest").json()['quote']
    label.config(text=kayne_quotes)


get_kayne_quotes()
label.grid(column=0, row=0, columnspan=3)
button = Button(text="Kayneee", command=get_kayne_quotes)
button.grid(row=1, column=1)
tk.mainloop()
