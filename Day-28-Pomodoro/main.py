from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 4
SECS_IN_MIN = 2
REPS_COUNT = 0
BREAK = False
STUDY_TEXT = 'STUDY TIME'
SHORT_BREAK_TEXT = 'SHORT BREAK'
LONG_BREAK_TEXT = 'LONG BREAK'
INITIAL_TEXT = "YOU READY?"
INITIAL_TIMER_STRING = '03:00'
timer = None
window = Tk()


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global timer, BREAK
    window.after_cancel(timer)
    BREAK = False
    checkmarks.config(text='')
    headline.config(text=INITIAL_TEXT)
    canvas.itemconfig(timer_text, text=INITIAL_TIMER_STRING)
# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_start():
    global REPS_COUNT
    if REPS_COUNT == 4:
        REPS_COUNT = 0
        headline.config(text=LONG_BREAK_TEXT, fg=RED)
        counter(LONG_BREAK_MIN * SECS_IN_MIN)
    elif BREAK:
        counter(SHORT_BREAK_MIN * SECS_IN_MIN)
        headline.config(text=SHORT_BREAK_TEXT, fg=PINK)
    else:
        counter(WORK_MIN * SECS_IN_MIN)
        headline.config(text=STUDY_TEXT, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def counter(amount):
    global BREAK, REPS_COUNT, timer
    count_mins = math.floor(amount / SECS_IN_MIN)
    count_secs = amount % SECS_IN_MIN
    canvas.itemconfig(timer_text, text=f'{str(count_mins).zfill(2)}:{str(count_secs).zfill(2)}')

    print(amount)
    if amount > 0:
        timer = window.after(1000, counter, amount - 1)
    if amount == 0:
        BREAK = not BREAK
        REPS_COUNT += 1 if BREAK else 0
        timer_start()
        checkmarks.config(text=f'{REPS_COUNT * "✅"}')

        # ---------------------------- UI SETUP ------------------------------- #


window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)

headline = Label(text=INITIAL_TEXT, bg=YELLOW, fg=GREEN, font=(FONT_NAME, '24', 'bold'))
headline.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=timer_start)
start.grid(row=2, column=0)

checkmarks = Label(text="", fg=GREEN, bg=YELLOW)
checkmarks.grid(row=3, column=1)

reset = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset.grid(row=2, column=2)

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text=INITIAL_TIMER_STRING, fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)
window.mainloop()
