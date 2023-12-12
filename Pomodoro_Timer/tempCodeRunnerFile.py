from tkinter import *
import math
import os

# Initialize Constants
GREEN = "#029557"
LIGHT_PURPLE = "#D5B5FC"
FONT_NAME = "Average"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# This function will load the image file
def load_image(file_name):
    try:
        # Get the current script directory
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, file_name)
        
        # Check if the file exists
        if os.path.exists(file_path):
            return PhotoImage(file=file_path)
        else:
            raise FileNotFoundError(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

# Function to start the timer mechanism
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine the timer's duration
    # Long Break
    if reps % 8 == 0:
        count_down(long_break_sec) 
        title_label.config(text="Break", fg=GREEN)  
    
    # Short Break
    elif reps % 2 == 0:
        count_down(short_break_sec)  
        title_label.config(text="Break", fg=GREEN)  
    
    # Work Time
    else:
        count_down(work_sec)  
        title_label.config(text="Work", fg=GREEN)

# Function to reset the timer
def reset_timer():
    window.after_cancel(timer)  # Cancel the timer
    canvas.itemconfig(timer_text, text="00:00")  # Reset the timer text on the canvas
    title_label.config(text="Timer")  # Reset the title label
    check_marks.config(text="")  # Clear check marks
    global reps
    reps = 0  # Reset reps counter
    pass
  
# Function for the countdown mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# Set Up User Interface
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=LIGHT_PURPLE)

title_label = Label(text="Timer",
                    fg=GREEN,
                    bg=LIGHT_PURPLE,
                    font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=LIGHT_PURPLE, highlightthickness=0)

# Load the image using the 'load_image' function
tomato_img = load_image("tomato.png")

if tomato_img:
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(100,
                                    130,
                                    text="00:00",
                                    fill="white",
                                    font=(FONT_NAME, 35, "bold"))
else:
    # If the image wasn't loaded, create a placeholder text
    canvas.create_text(100, 112, text="Image not found", fill="white")

canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=LIGHT_PURPLE)
check_marks.grid(column=1, row=3)

# Execute GUI
window.mainloop()
