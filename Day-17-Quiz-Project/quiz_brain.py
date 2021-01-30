class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number].question
        current_answer = self.question_list[self.question_number].answer.lower()
        if self.question_number > 0:
            print(f'Total Score {self.question_number}/{self.question_number}')

        reply_valid = False
        while not reply_valid:
            question = input(f"Q.{self.question_number+1}: {current_question} (True/False):  ").lower()
            if question != 'true' and question != 'false':
                print("Please either write 'true' or 'false'.\n")
            else:
                reply_valid = True

        def check_if_end():
            if self.question_number == len(self.question_list):
                return False
            else:
                return True

        if question == current_answer:
            print(f"You got it right!\nThe Statement was in fact {current_answer}\n")
            self.question_number += 1

            if check_if_end():
                self.next_question()
            else:
                print(f"Game ended.\nFinal Score: {self.question_number}/{self.question_number}")
        else:
            self.question_number -= 1
            return print(f"\nSorry incorrect ans\nFinal Score: {self.question_number}/{self.question_number+1}")
