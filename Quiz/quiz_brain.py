class QuizBrain:
    # Initialize QuizBrain with question number, score, and question list
    def __init__(self, q_list):
        # Track the current question number
        self.question_number = 0  
        # Track the current score
        self.score = 0  
        # Store the list of questions
        self.question_list = q_list  

    # Check if there are remaining questions in the list
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Present the next question to the user
    def next_question(self):
        # Get the current question
        current_question = self.question_list[self.question_number]  
        # Move to the next question
        self.question_number += 1  
        # Ask for user's answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")  
        # Check the user's answer
        self.check_answer(user_answer, current_question.answer)  

    def check_answer(self, user_answer, correct_answer):
        # Check if the user's answer matches the correct answer and update the score
        if user_answer.lower() == correct_answer.lower():
            # Increase the score if the answer is correct
            self.score += 1  
            print("You got it right!")
        else:
            print("That's wrong.")
        # Display the correct answer
        print(f"The correct answer was: {correct_answer}.")  
        # Display current score
        print(f"Your current score is: {self.score}/{self.question_number}")  
        # Add a newline for readability
        print("\n")  
