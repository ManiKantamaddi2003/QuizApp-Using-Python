class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.remaining_pass = 2
        self.question_list = q_list


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}? (True/False/Pass/Off): ").capitalize()

        while user_answer != "True" and user_answer != "False" and user_answer != "Off" and user_answer != "Pass":
            print(f"\n\tYou entered a wrong value({user_answer})\n")
            user_answer = input(f"Q.{self.question_number}: {current_question.text}? (True/False/Pass/Off): ").capitalize()

        if user_answer == "Off":
            print(f"\n\tYour final score is {self.score}/{self.question_number - 1}\n")
            print("\tBye...")
            return False
        elif user_answer == "Pass":
            if self.remaining_pass > 0:
                self.remaining_pass -= 1
                print(f"\n\tQuestion {self.question_number} was passed.")
                print(f"\tYour remaining pass right is {self.remaining_pass}\n")
            else:
                print("\n\tYour pass is over.\n")
                self.question_number -= 1
            return True
        else:
            self.check_answer(user_answer, current_question.answer)
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("\n\tYou got it right!")
        else:
            print("\n\tYou are wrong!")

        print(f"\tThe correct answer was {correct_answer}")

        if self.question_number < len(self.question_list):
            print(f"\tYour current score is {self.score}/{self.question_number}")
            print(f"\tYour remaining pass right is {self.remaining_pass}\n")


