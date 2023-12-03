import html

class QuizBrain:
    # Constructor to initialize QuizBrain object with necessary attributes
    def __init__(self, q_list):
        self.question_number = 0  # Attribute to track current question number
        self.score = 0  # Attribute to store the user's score
        self.question_list = q_list  # Attribute to store the list of questions
        self.current_question = None  # Attribute to store the current question object

    # Method to check if there are still questions remaining in the question list
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Method to get the next question in the quiz
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Decode HTML entities in the question text using html.unescape()
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"  # Return the formatted question number and text

    # Method to check the user's answer against the correct answer
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        # Check if the user's answer matches the correct answer (case-insensitive)
        if user_answer.lower() == correct_answer.lower():
            self.score += 1  # Increment the score if the answer is correct
            return True  # Return True if the answer is correct
        else:
            return False  # Return False if the answer is incorrect
