from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text=f"Score: {NONE}", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)

        self.text = self.canvas.create_text(150,
                                            125,
                                            width=280,
                                            text="Title",
                                            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_img = PhotoImage(file="images//true.png")
        self.button_right = Button(image=right_img,
                                   highlightthickness=0,
                                   borderwidth=0,
                                   command=self.true_answer
                                   )
        self.button_right.grid(column=0, row=2)

        wrong_img = PhotoImage(file="images//false.png")
        self.button_wrong = Button(image=wrong_img,
                                   highlightthickness=0,
                                   borderwidth=0,
                                   command=self.false_answer
                                   )
        self.button_wrong.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the Quiz.")
            self.button_wrong.config(state="disabled")
            self.button_right.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



