# Authenication
''' The code creates an authentication system for the user. '''

''' 
Values to change in code
    1) secret-key-goes-here in line 17 to create a secret key when managing sessions
'''

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Initialize Flask application
app = Flask(__name__)
# Set the secret key for session management
app.config['SECRET_KEY'] = 'secret-key-goes-here'  

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
    return User.query.get(int(user_id))

# Define the User table in the database
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# Create all tables within the database
with app.app_context():
    db.create_all()

# Routes
# Homepage
@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

# User Registration
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("That email address is already in use")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(email=email, password=hashed_password, name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("register.html", logged_in=current_user.is_authenticated)

# User Login
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Invalid email or password')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)

# Protected route that requires authentication
@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)

# User Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Route to download a file when the user is logged in
@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")

# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)