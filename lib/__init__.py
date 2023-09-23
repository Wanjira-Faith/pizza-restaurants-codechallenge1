from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from lib import routes

if __name__ == '__main__':
    app.run(debug=True)