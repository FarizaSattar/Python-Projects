# Typing Speed Test

''' The code allows the user to perform a test to measure their typing speed. '''

import tkinter as tk  
import random  
import time  

def start_test():
    global start_time
    # Define the text for the typing test
    text_to_type = "The quick brown fox jumps over the lazy dog"
    random.shuffle(alphabet)  # Shuffle alphabet for a randomized typing experience
    text_label.config(text=text_to_type, font=("Arial", 14))  # Set the text to display for typing

    start_time = time.time()  # Record the starting time of the typing test
    entry.focus_set()  # Set focus to the entry field for typing
    start_button.config(state=tk.DISABLED)  # Disable the start button after starting the test

def check_text(event):
    global start_time
    typed_text = entry.get()  # Get the typed text from the entry field
    entry.delete(0, tk.END)  # Clear the entry field for the next input

    if typed_text == text_label.cget("text"):  # Check if typed text matches the given text
        end_time = time.time()  # Record the ending time of the typing test
        elapsed_time = end_time - start_time  # Calculate the elapsed time for typing
        # Calculate typing speed in words per minute and display the result
        words_per_minute = len(text_label.cget("text")) / (elapsed_time / 60)
        result_label.config(text=f"Your typing speed is {words_per_minute:.2f} words per minute.")
        start_button.config(state=tk.NORMAL)  # Enable the start button for another test
    else:
        result_label.config(text="Incorrect typing. Try again.")  # Display error message for incorrect typing

# Tkinter GUI setup
root = tk.Tk()  # Create the main Tkinter window
root.title("Typing Speed Test")  # Set the title of the window

alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
random.shuffle(alphabet)  # Shuffle alphabet for variety in typing

text_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)  # Label to display text for typing
text_label.pack(pady=20)  # Place the text label in the window

entry = tk.Entry(root, font=("Arial", 12))  # Entry field for typing
entry.pack(pady=10)  # Place the entry field in the window
entry.bind("<Return>", check_text)  # Bind Enter key to check the typed text

start_button = tk.Button(root, text="Start Test", command=start_test)  # Button to start the typing test
start_button.pack(pady=10)  # Place the start button in the window

result_label = tk.Label(root, text="", font=("Arial", 12))  # Label to display typing speed result
result_label.pack(pady=10)  # Place the result label in the window

root.mainloop()  # Run the Tkinter event loop to display the GUI and handle user interactions
