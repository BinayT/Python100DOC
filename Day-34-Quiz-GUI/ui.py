from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz):
        self.window = Tk()
        self.quiz = quiz
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = self.quiz.score
        self.score_label = Label(text=f"Score: {self.score}/10")
        self.score_label.config(bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, width=280, font=("Arial", 20, 'italic'),
                                                   text="")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.false_ans)
        self.wrong_button.grid(row=2, column=0)
        true_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=true_image, highlightthickness=0, command=self.true_ans)
        self.right_button.grid(row=2, column=1)
        self.show_question()
        self.window.mainloop()

    def show_question(self):
        text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=text)

    def check_final_question(self):
        if not self.quiz.still_has_questions():
            if self.score >= 8:
                text = f"You got {self.score}. Super DAMN INTELLIGENT."
            elif 5 < self.score < 8:
                text = f"You got {self.score}. Not bad ;)."
            else:
                text = f"You got {self.score}. Got to improve :P."
            self.canvas.itemconfig(self.canvas_text, text=text)
            return False
        else:
            print(self.score)
            return True

    def false_ans(self):
        if self.check_final_question():
            self.show_question()
        else:
            self.wrong_button['state'] = DISABLED
            self.right_button['state'] = DISABLED

    def true_ans(self):
        if self.check_final_question():
            self.score = self.quiz.check_answer('True')
            self.score_label.config(text=f"Score: {self.score}/10")
            self.show_question()
        else:
            self.wrong_button['state'] = DISABLED
            self.right_button['state'] = DISABLED
