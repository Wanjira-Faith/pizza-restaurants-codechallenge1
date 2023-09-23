from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
from models import db

# Create a Flask application instance
app = Flask(__name__)