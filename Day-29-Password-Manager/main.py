from tkinter import *
from password_gen import random_password_generator

RANDOM_PASSWORD = None
window = Tk()
window.title('Password Manager')
window.config(padx=100, pady=50)

# Random password generator


def create_password():
    global RANDOM_PASSWORD
    RANDOM_PASSWORD = random_password_generator()
    print(RANDOM_PASSWORD)

# LOGO
logo = Canvas(height=224, width=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
logo.create_image(110, 112, image=logo_img)
logo.grid(column=1, row=0)

# Labels and Entries
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.grid(column=1, row=1)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(column=0, row=2)
email_entry = Entry()
email_entry.grid(column=1, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3)
password_generate_button = Button(text="Generate Password", command=create_password)
password_generate_button.grid(column=2, row=3)

add_button = Button(text="Add")
add_button.grid(column=1, row=4)


window.mainloop()
