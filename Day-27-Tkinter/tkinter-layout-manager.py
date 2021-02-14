from tkinter import *

window = Tk()
window.title("My practice")
window.minsize(500,500)

label = Label(text="A label tag", font=("Arial", 24))
label.grid(column=0, row=0)

button = Button(text="Button 1")
button.grid(column=1, row=1)

button1 = Button(text="Button 2")
button1.grid(column=3, row=0)

entry = Entry()
entry.grid(column=4, row=2)
window.mainloop()