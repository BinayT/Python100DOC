from tkinter import *
import requests
kayne_quotes = None

tk = Tk()
tk.title("Kayne Quotes")
tk.config(padx=100, pady=100)

label = Label(text='', font=("Courier", 22, 'bold'))
canvas = Canvas(height=300, width=400, highlightthickness=0)
kayne_logo = PhotoImage(file='Kayne-API/kaynelogo.png')
canvas.create_image(200, 150, image=kayne_logo)
kayne_quote = canvas.create_text(200, 50, width=400, text="", font=("Arial", 18, 'italic'))
canvas.grid(column=0, row=0, columnspan=3)


def get_kayne_quotes():
    global kayne_quotes
    kayne_quotes = requests.get("https://api.kanye.rest").json()['quote']
    canvas.itemconfig(kayne_quote, text=kayne_quotes)
    label.config(text=kayne_quotes)


get_kayne_quotes()
button = Button(text="Kayneee", command=get_kayne_quotes)
button.grid(row=1, column=1)
tk.mainloop()
