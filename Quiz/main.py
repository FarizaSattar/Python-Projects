# Quiz

''' The code creates a quiz for the user. '''

# Import necessary classes
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create an empty list to store Question objects
question_bank = []

# Iterate through the question_data list to create Question objects and add them to the question_bank list
for question in question_data:
    # Extract the text of the question
    question_text = question["question"] 
    # Extract the correct answer for the question
    question_answer = question["correct_answer"]  
    # Create a new Question object
    new_question = Question(question_text, question_answer)  
    # Add the new Question object to the question_bank list
    question_bank.append(new_question)  

# Create a QuizBrain object and pass the question_bank list to it
quiz = QuizBrain(question_bank)

# Continue asking questions until there are no more questions left
while quiz.still_has_questions():
    # Ask the next question in the quiz
    quiz.next_question()  

# Display completion message along with the user's final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
