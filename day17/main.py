from question_model import Question
from data import question_data
from quiz_brain import QuizeBrain


question_bank = []

for question in question_data:
    text_question = question["question"]
    text_answer = question["answer"]
    new_question = Question(text_question, text_answer)
    question_bank.append(new_question)

quiz = QuizeBrain(question_bank)
while quiz.still_has_question:
    quiz.next_question()

print("Your completed the quiz💪")
print(f"Your finel score is {quiz.score}/{len(question_bank)}")
