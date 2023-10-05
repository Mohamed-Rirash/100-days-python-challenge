#TODO: asking the question
#TODO: checking if the answer was correct 
#TODO: check if we ware the end of the quiz


## clss name QuizeBrain
## question_number = 0;
## question_number list

## methode next_question()

class QuizeBrain:
    def __init__(self,q_list):
      self.question_number = 0
      self.question_list = q_list
      self.score = 0
      
    current_question = ""

    def still_has_question(self):
        return self.question_number < len(self.question_list)
          


    def next_question(self):
        current_question = self.question_list[self.question_number - 1]
        self.question_number += 1
        user_answer = input(f"q.{self.question_number}: {current_question.text} (true/false): ").lower()
        self.check_user_answer(user_answer,current_question.answer)


    def check_user_answer(self, user_answer, correct_answer):
        if user_answer.lower() == str(correct_answer).lower():
            self.score += 1
            print("you got it right!")
        else:
            print("that`s wrong!")
            print(f"the correct anser was: {correct_answer}!")
            print(f"Your current is score is {self.score}/{self.question_number}")
            print("\n")
            exit()
