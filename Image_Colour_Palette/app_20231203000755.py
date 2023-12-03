# Image Colour Palette

from flask import Flask, render_template, request
from PIL import Image
import io
from collections import Counter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['image']
    if uploaded_file.filename != '':
        img = Image.open(io.BytesIO(uploaded_file.read()))
        img = img.convert('RGB')
        img.thumbnail((200, 200))  # Resize image for faster processing

        # Get the most common colors
        colors = img.getcolors(img.width * img.height)
        if colors:
            sorted_colors = sorted(colors, key=lambda x: -x[0])[:10]  # Get top 10 colors
            return render_template('index.html', colors=sorted_colors)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
