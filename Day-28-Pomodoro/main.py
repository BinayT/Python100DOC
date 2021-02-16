from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
window = Tk()

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_counter():
    timer_func()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


minutes = 25
sec = 0
counts = 0
study = True


def timer_func():
    global minutes, sec, counts, study
    canvas.itemconfig(timer_text, text=f'{minutes}:{sec}')

    if minutes == 0 and sec == 0:
        study = not study
        if study:
            minutes = 25
        else:
            minutes = 5

    if minutes == 0 and sec == 0:
        canvas.itemconfig(timer_text, text=f'{minutes}:{sec}')

    if sec == 0:
        sec = 60
        minutes -= 1
    sec -= 1
    window.after(1000, timer_func)
    print(f'min:{minutes} sec:{sec}')


# ---------------------------- UI SETUP ------------------------------- #

window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)


timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, '24', 'bold'))
timer.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_counter)
start.grid(row=2, column=0)

label = Label(text="✅", fg=GREEN, bg=YELLOW)
label.grid(row=3, column=1)

reset = Button(text="Reset", highlightthickness=0)
reset.grid(row=2, column=2)

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()