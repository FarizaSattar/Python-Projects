# Image Colour Palette

''' The code allows the user to upload an image, and display 
the top 10 most common colors in it. '''

from flask import Flask, render_template, request
from PIL import Image
import io
from collections import Counter

# Create a Flask web application instance named 'app'
app = Flask(__name__)  

# Define a route for the root URL '/'
@app.route('/')  
def index():

    # Render the 'index.html' template when accessing the root URL
    return render_template('index.html')  

# Define a route for '/upload' that accepts POST requests
@app.route('/upload', methods=['POST'])  
def upload():
    # Get the uploaded image file
    uploaded_file = request.files['image']  
    if uploaded_file.filename != '':
        # Open the uploaded image file
        img = Image.open(io.BytesIO(uploaded_file.read()))  
        # Convert image to RGB format
        img = img.convert('RGB')  
        # Resize image for faster processing
        img.thumbnail((200, 200))  

        # Count occurrences of each color
        colors = img.getcolors(img.width * img.height)  
        if colors:
            # Get top 10 most common colors
            sorted_colors = sorted(colors, key=lambda x: -x[0])[:10]  
            # Render 'index.html' with top colors
            return render_template('index.html', colors=sorted_colors)  

    # Render 'index.html' if no image uploaded or processed
    return render_template('index.html')  

if __name__ == '__main__':
    # Run the Flask app in debug mode if this script is executed directly
    app.run(debug=True)  
