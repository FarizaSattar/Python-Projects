# Cafe API

''' The code sets up a Flask web application utilizing SQLAlchemy to manage a database of cafes, allowing 
users to perform CRUD operations, including retrieving a random cafe, fetching all cafes, searching for cafes 
by location, adding new cafes, updating cafe prices, and deleting cafes using different HTTP methods and 
routes. '''

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

# Install the required packages first: Open the Terminal in PyCharm.
# On Windows, type: python -m pip install -r requirements.txt
# On MacOS, type: pip3 install -r requirements.txt
# This will install the packages from requirements.txt for this project.

app = Flask(__name__)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

##CREATE TABLE
class Cafe(db.Model):
    # Define the structure of the Cafe table.
    # (Column names, types, constraints)
    # Define method to convert data to dictionary format.
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    # Rest of the code defines different routes and operations
    # for managing the cafes in the database.

if __name__ == '__main__':
    app.run(debug=True)
