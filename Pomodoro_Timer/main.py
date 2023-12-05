# Pomodoro Timer

''' The code creates a graphical Pomodoro Timer using tkinter, with functionality to set work and break 
intervals, initiate countdowns, display sessions, and facilitate reset and start functionalities through 
button controls. '''

from tkinter import *  # Import the necessary components from the tkinter library
import math

# Constants defining colors, font, and time intervals
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Function to reset the timer
def reset_timer():
    window.after_cancel(timer)  # Cancel the timer
    canvas.itemconfig(timer_text, text="00:00")  # Reset the timer text on the canvas
    title_label.config(text="Timer")  # Reset the title label
    check_marks.config(text="")  # Clear check marks
    global reps
    reps = 0  # Reset reps counter

# Function to start the timer mechanism
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)  # Initiate countdown for a long break
        title_label.config(text="Break", fg=RED)  # Change title label to "Break"
    elif reps % 2 == 0:
        count_down(short_break_sec)  # Initiate countdown for a short break
        title_label.config(text="Break", fg=PINK)  # Change title label to "Break"
    else:
        count_down(work_sec)  # Initiate countdown for work duration
        title_label.config(text="Work", fg=GREEN)  # Change title label to "Work"

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

# User Interface Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()  # Start the GUI execution
