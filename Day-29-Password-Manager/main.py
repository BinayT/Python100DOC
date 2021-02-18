from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx=100, pady=50)

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
password_generate_button = Button(text="Generate Password")
password_generate_button.grid(column=2, row=3)


window.mainloop()
