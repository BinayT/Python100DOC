from tkinter import *
from tkinter import messagebox as mb
from password_gen import random_password_generator
import json

RANDOM_PASSWORD = None
window = Tk()
window.title('Password Manager')
window.config(padx=100, pady=50)


def create_password():
    global RANDOM_PASSWORD
    RANDOM_PASSWORD = random_password_generator()
    password_entry.insert(END, RANDOM_PASSWORD)


def add_to_file():
    website = website_entry.get().lower()
    password = password_entry.get()
    email = email_entry.get()
    obj_to_save = {website: {'password': password, 'email': email}}

    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        mb.showinfo("Opps", "Please make sure you didn't leave anything empty")
    else:
        if mb.askyesno('Final Step', 'You sure the data are correct?'):
            with open('password.json', mode='w') as password_file:
                json.dump(obj_to_save, password_file, indent=4)
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.delete(0, 'end')


logo = Canvas(height=224, width=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
logo.create_image(110, 112, image=logo_img)
logo.grid(column=1, row=0)

# Labels and Entries
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.grid(column=1, row=1)

search_button = Button(text="Search", command=add_to_file)
search_button.grid(column=2, row=1)

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

add_button = Button(text="Add", command=add_to_file)
add_button.grid(column=1, row=4)

window.mainloop()