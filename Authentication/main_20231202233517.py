# Authenication

''' The code establishes an authentication system in a Flask application using SQLAlchemy and Flask-Login, 
including user registration, login, logout functionalities, secret page access, and file download, ensuring 
password security by hashing and salting the passwords before storing them in the database. '''

# Import necessary modules and libraries
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'  # Set the secret key for session management

# Connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# Initialize Flask-Login for managing user sessions
login_manager = LoginManager()
login_manager.init_app(app)

# Function to load a user
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# Define the User table in the database
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# Create all tables within the database
with app.app_context():
    db.create_all()

# Define routes for different functionalities

# Homepage
@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

# User registration
@app.route('/register', methods=["GET", "POST"])
def register():
    # Registration logic
    # ... (code to handle registration)

# User login
@app.route('/login', methods=["GET", "POST"])
def login():
    # Login logic
    # ... (code to handle user login)

# Protected route requiring authentication
@app.route('/secrets')
@login_required
def secrets():
    # Accessing protected content
    # ... (code to access and display secrets)

# User logout
@app.route('/logout')
@login_required
def logout():
    # Logout logic
    # ... (code to handle user logout)

# Route to download a file (accessible only when logged in)
@app.route('/download')
@login_required
def download():
    # Logic to handle file download
    # ... (code to download a file)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

