from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx=100, pady=50)

logo = Canvas(height=224, width=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
logo.create_image(110, 112, image=logo_img)
logo.grid(column=1, row=1)

window.mainloop()
