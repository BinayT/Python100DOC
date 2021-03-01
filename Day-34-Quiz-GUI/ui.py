from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}")
        self.score_label.config(bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, width=300, font=("Arial", 20, 'italic'),
                                                   text="Hello there")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image, highlightthickness=0)
        self.wrong_button.grid(row=2, column=0)
        true_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=true_image, highlightthickness=0)
        self.right_button.grid(row=2, column=1)
        self.window.mainloop()

