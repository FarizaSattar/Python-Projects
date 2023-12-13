# Image Watermarking
''' The code allows users to upload an image, apply a specified text watermark on the image, and display it. '''

'''
Values to change in code
  1) "Your Watermark Here" in line 29 with your watermark
'''

import tkinter as tk  
from tkinter import filedialog  
from PIL import Image, ImageDraw, ImageFont  

# Function to prompt user to select an image file
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        # If an image file is selected, open it and process the image
        original_image = Image.open(file_path)
        process_image(original_image)

# Function to add a text watermark to the image
def process_image(image):
    # Replace with your desired watermark text
    watermark_text = "Your Watermark Here"  
    # Font and size for the watermark
    watermark_font = ImageFont.truetype("arial.ttf", 36)  
    draw = ImageDraw.Draw(image)
    # Position and color for the watermark
    draw.text((10, 10), watermark_text, fill="white", font=watermark_font)  
    # Display the image with the watermark (you can also save it using image.save)
    image.show()  

# Create the main Tkinter window
root = tk.Tk()  
# Set the title of the window
root.title("Image Watermark App")  

# Create a button to trigger the image upload function and display it in the window
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=20)  

# Run the Tkinter event loop to display the GUI and handle user interactions
root.mainloop()  
