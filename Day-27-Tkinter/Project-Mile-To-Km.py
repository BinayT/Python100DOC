from tkinter import *

window = Tk()
window.title("Mile to Km")
window.minsize(width=300, height=300)

entry = Entry(width=10)
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to ")
label2.grid(column=0, row=1)

label3 = Label(text='0')
label3.grid(column=1, row=1)

label2 = Label(text="KM")
label1.grid(column=2, row=1)


def calculate_kms():
    label3['text'] = int(entry.get())*1.61
    # text_to_write = int(entry.get()) * 1.61
    # entry2['text'] = text_to_write


button = Button(text="Calculate", command=calculate_kms)
button.grid(column=1, row=2)

window.mainloop()