from tkinter import Tk, Label

window = Tk()

window.title("My program")
window.minsize(height=500, width=500)

my_label = Label(text="I am a Label", font=("Courier", 24, 'bold'))
my_label.pack(side="left")

window.mainloop()