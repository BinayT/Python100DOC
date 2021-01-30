from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    new_question_model = Question(question_data[i]['text'], question_data[i]['answer'])
    question_bank.append(new_question_model)

heya = QuizBrain(question_bank)
heya.next_question()