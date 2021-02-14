from tkinter import *

window = Tk()

window.title("My program")
window.minsize(height=500, width=500)

my_label = Label(text="I am a Label", font=("Courier", 24, 'bold'))
my_label.pack()

inputt = Entry(width= 80)
inputt.pack()


def button_clicked():
    my_label['text'] = inputt.get()


button = Button(text="YO MAMA", command=button_clicked)
button.pack()


window.mainloop()