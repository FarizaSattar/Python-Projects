from flask import Flask, render_template

app = Flask(__name__)

# Cafe data (this could be stored in a database in a real application)
cafes = [
    {
        'name': 'Cafe A',
        'location': '123 Main St, City',
        'wifi': True,
        'power': True
    },
    {
        'name': 'Cafe B',
        'location': '456 Elm St, Town',
        'wifi': True,
        'power': False
    },
    # Add more cafe data as needed
]

@app.route('/')
def index():
    return render_template('index.html', cafes=cafes)

if __name__ == '__main__':
    app.run(debug=True)
