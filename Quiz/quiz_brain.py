class QuizBrain:
    def __init__(self, q_list):
        # Initialize QuizBrain with question number, score, and question list
        self.question_number = 0  # Track the current question number
        self.score = 0  # Track the current score
        self.question_list = q_list  # Store the list of questions

    def still_has_questions(self):
        # Check if there are remaining questions in the list
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Present the next question to the user
        current_question = self.question_list[self.question_number]  # Get the current question
        self.question_number += 1  # Move to the next question
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")  # Ask for user's answer
        self.check_answer(user_answer, current_question.answer)  # Check the user's answer

    def check_answer(self, user_answer, correct_answer):
        # Check if the user's answer matches the correct answer and update the score
        if user_answer.lower() == correct_answer.lower():
            self.score += 1  # Increase the score if the answer is correct
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")  # Display the correct answer
        print(f"Your current score is: {self.score}/{self.question_number}")  # Display current score
        print("\n")  # Add a newline for readability
