from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create a Flask application instance
app = Flask(__name__)

# Configure database URI and disable track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration objects
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize database with the Flask app
db.init_app(app)

from models import Restaurant, Pizza, RestaurantPizza
from app import routes

if __name__ == '__main__':
    app.run(debug=True)