from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
from models import db  

# Create a Flask application instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if __name__ == '__main__':
    app.run(debug=True)
