# Quiz

''' The code creates a quiz from a set of questions, iterates through them, prompting the user to answer each 
question, and finally displays the user's quiz score. '''

# Import necessary classes
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create an empty list to store Question objects
question_bank = []

# Iterate through the question_data list to create Question objects and add them to the question_bank list
for question in question_data:
    question_text = question["question"]  # Extract the text of the question
    question_answer = question["correct_answer"]  # Extract the correct answer for the question
    new_question = Question(question_text, question_answer)  # Create a new Question object
    question_bank.append(new_question)  # Add the new Question object to the question_bank list

# Create a QuizBrain object and pass the question_bank list to it
quiz = QuizBrain(question_bank)

# Continue asking questions until there are no more questions left
while quiz.still_has_questions():
    quiz.next_question()  # Ask the next question in the quiz

# Display completion message along with the user's final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
