# Todo List

''' The code establishes a Flask web application that utilizes SQLite to create a 'tasks' table, allowing 
users to add, display, and delete tasks via different routes ('/', '/add', '/delete/int:id') and associated 
functions in response to HTTP requests. '''

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create a connection to the database
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Create a table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)''')
conn.commit()

@app.route('/')
def index():
    c.execute('''SELECT * FROM tasks ORDER BY id DESC''')
    tasks = c.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    c.execute('''INSERT INTO tasks (task) VALUES (?)''', (task,))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    c.execute('''DELETE FROM tasks WHERE id=?''', (id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
