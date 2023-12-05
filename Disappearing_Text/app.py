# Disappearing Text

''' The code sets up a Flask web application with a single route that renders an HTML template named 
'index.html' when accessing the root URL ('/') and runs the app in debug mode if executed directly. '''

from flask import Flask, render_template, request

app = Flask(__name__)  # Create a Flask web application instance named 'app'

@app.route('/')  # Define a route for the root URL '/'
def index():
    return render_template('index.html')  # Render the 'index.html' template when accessing the root URL

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode if this script is executed directly
