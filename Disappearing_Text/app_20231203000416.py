# Disappearing Text

''' The code sets up a Flask web application with a single route that renders an HTML template named 
'index.html' when accessing the root URL ('/') and runs the app in debug mode if executed directly. '''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
