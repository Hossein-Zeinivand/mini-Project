from data import question_data
from question_model import Question
from Quiz_Brain import QuizBrain


question_bank = list()
for question in question_data:
    new_question = Question(question["question"],question["correct_answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)


while quiz_brain.still_has_question():
    quiz_brain.nex_question()
