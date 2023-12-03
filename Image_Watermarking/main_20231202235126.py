# Image Watermarking

''' The code creates a basic Tkinter-based desktop application in Python allowing users to upload an image, 
apply a specified text watermark on the image, and display the watermarked image within the GUI window. '''

import tkinter as tk  # Importing Tkinter for GUI creation
from tkinter import filedialog  # Importing filedialog for file selection
from PIL import Image, ImageDraw, ImageFont  # Importing necessary PIL modules for image processing

def upload_image():
    # Function to prompt user to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        # If an image file is selected, open it and process the image
        original_image = Image.open(file_path)
        process_image(original_image)

def process_image(image):
    # Function to add a text watermark to the image
    watermark_text = "Your Watermark Here"  # Replace with your desired watermark text
    watermark_font = ImageFont.truetype("arial.ttf", 36)  # Font and size for the watermark
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), watermark_text, fill="white", font=watermark_font)  # Position and color for the watermark
    image.show()  # Display the image with the watermark (you can also save it using image.save)

# Tkinter GUI setup
root = tk.Tk()  # Create the main Tkinter window
root.title("Image Watermark App")  # Set the title of the window

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=20)  # Create a button to trigger the image upload function and display it in the window

root.mainloop()  # Run the Tkinter event loop to display the GUI and handle user interactions
