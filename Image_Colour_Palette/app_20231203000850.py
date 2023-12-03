# Image Colour Palette

''' The script creates a website allowing users to upload an image, then processes it to identify and display 
the top 10 most common colors present in the image. '''

from flask import Flask, render_template, request
from PIL import Image
import io
from collections import Counter

app = Flask(__name__)  # Create a Flask web application instance named 'app'

@app.route('/')  # Define a route for the root URL '/'
def index():
    return render_template('index.html')  # Render the 'index.html' template when accessing the root URL

@app.route('/upload', methods=['POST'])  # Define a route for '/upload' that accepts POST requests
def upload():
    uploaded_file = request.files['image']  # Get the uploaded image file
    if uploaded_file.filename != '':
        img = Image.open(io.BytesIO(uploaded_file.read()))  # Open the uploaded image file
        img = img.convert('RGB')  # Convert image to RGB format
        img.thumbnail((200, 200))  # Resize image for faster processing

        # Get the most common colors
        colors = img.getcolors(img.width * img.height)  # Count occurrences of each color
        if colors:
            sorted_colors = sorted(colors, key=lambda x: -x[0])[:10]  # Get top 10 most common colors
            return render_template('index.html', colors=sorted_colors)  # Render 'index.html' with top colors
    
    return render_template('index.html')  # Render 'index.html' if no image uploaded or processed

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode if this script is executed directly
