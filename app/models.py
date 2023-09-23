from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255))
    
    # Define the many-to-many relationship with Pizza through the restaurant_pizza association table
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')
       
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f'<Restaurant {self.id}: {self.name}'    

    def validate(self):
        errors = {}

        if not self.name:
            errors['name'] = 'Name is required'

        if len(self.name) > 50:
            errors['name'] = 'Name must be less than 50 characters long'

        return errors    
     
class Pizza(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

   # Define the many-to-many relationship with Restaurant through the restaurant_pizza association table 
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', back_populates='pizzas')

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __repr__(self):
        return f'<Pizza {self.id}: {self.name}'   

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float(asdecimal=True))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Define relationships with Restaurant and Pizza
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='pizza_restaurants')

    def __init__(self, price, restaurant_id, pizza_id):
        self.price = price
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id

    def __repr__(self):
        return f'<RestaurantPizza {self.id}: Price: {self.price}>'    
    
    def validate(self):
        errors = {}

        if not self.price:
            errors['price'] = 'Price is required'

        if self.price < 1 or self.price > 30:
            errors['price'] = 'Price must be between 1 and 30'

        return errors