# Todo List

''' The code creates a Todo List for the user. '''

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create a connection to the SQLite database
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Create a 'tasks' table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)''')
conn.commit()

@app.route('/')
def index():
    # Retrieve tasks from the 'tasks' table and render them on the index page
    c.execute('''SELECT * FROM tasks ORDER BY id DESC''')
    tasks = c.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    # Add a new task to the 'tasks' table
    task = request.form['task']
    c.execute('''INSERT INTO tasks (task) VALUES (?)''', (task,))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    # Delete a task with the specified ID from the 'tasks' table
    c.execute('''DELETE FROM tasks WHERE id=?''', (id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
