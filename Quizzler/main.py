# Quizzler

''' The provided imports data for quiz questions, creates a quiz brain based on the provided questions, and 
initiates a user interface for the quiz. '''

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create an empty list to store Question objects
question_bank = []

# Extract data from question_data and create Question objects, then add them to question_bank
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a QuizBrain instance with the question bank
quiz = QuizBrain(question_bank)

# Initialize the user interface for the quiz using QuizInterface
quiz_ui = QuizInterface(quiz)
