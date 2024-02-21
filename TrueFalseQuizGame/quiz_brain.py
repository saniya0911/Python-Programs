class QuizBrain():
    def __init__(self, list):
        self.question_number = 0
        self.score = 0
        self.question_list = list

    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number+=1
        ans = input(f"Q.{self.question_number}: {item.text} (True/False): ").lower()
        self.check_answer(ans, item.answer)

    def still_has_questions(self):
        return self.question_number<len(self.question_list)
            
    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans.lower():
            self.score+=1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")