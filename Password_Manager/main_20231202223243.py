# Password Manager

''' The code is a Password Manager GUI created using Tkinter in Python, featuring functionalities for 
generating random passwords, saving website details (like website name, email, and password) to a file, and 
includes a graphical user interface for interaction and data entry. '''

from tkinter import *  # Import necessary modules
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Function to generate a password
def generate_password():
    # Define character sets for generating passwords
    letters = ['a', 'b', 'c', ... 'Y', 'Z']
    numbers = ['0', '1', '2', ... '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Create lists with random characters from each character set
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine the character lists and shuffle to create a strong password
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Convert the password list to a string and insert into the password entry field
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy password to clipboard for easy use

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get the website, email, and password entered by the user
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if website or password fields are empty and show an error message
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # Ask for confirmation to save entered details
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            # Save the entered details to a file and clear the entry fields
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()  # Create the main window
window.title("Password Manager")  # Set window title
window.config(padx=50, pady=50)  # Configure window padding

canvas = Canvas(height=200, width=200)  # Create canvas for logo
logo_img = PhotoImage(file="logo.png")  # Load logo image
canvas.create_image(100, 100, image=logo_img)  # Place logo image on canvas
canvas.grid(row=0, column=1)  # Place canvas in the window

# Labels for website, email, and password fields
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry fields for website, email, and password
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")  # Default email inserted
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons for generating password and saving details
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()  # Start the main loop to run the application
