from tkinter import *
import requests # This is used to make API calls, similar axios library in JavaScript
kayne_quotes = None

# Here I'm creating Tkinter windows
tk = Tk()
tk.title("Kayne Quotes")
tk.config(padx=100, pady=100)

# Here I'm creating a canvas, where I will put kayne's photo as bg and his quotes above it.
canvas = Canvas(height=300, width=400, highlightthickness=0)
kayne_logo = PhotoImage(file='Kayne-API/kaynelogo.png')
canvas.create_image(200, 150, image=kayne_logo)
kayne_quote = canvas.create_text(200, 50, width=400, text="", font=("Arial", 18, 'italic'))
canvas.grid(column=0, row=0, columnspan=3)


def get_kayne_quotes():
    global kayne_quotes
    # Here I'm making API request and directly getting it's JSON format and getting the 'quote' value of it.
    kayne_quotes = requests.get("https://api.kanye.rest").json()['quote']
    # And here I replace the text of canvas with the kayne quotes, like I'd do with document.getelementbyid() in JS
    canvas.itemconfig(kayne_quote, text=kayne_quotes)

# I call the function beforehand to actually load the program with kayne quotes pre-shown in the UI
get_kayne_quotes()

button_logo = PhotoImage(file="Kayne-API/kaynebutton.png")
# Here I Made a button and connected it to the command to fetch a new kayne quote + made the button an Image of Kayne
button = Button(image=button_logo, command=get_kayne_quotes)
button.grid(row=1, column=1)
# This function keeps running+checking for changes in our app.
tk.mainloop()
