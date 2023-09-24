from faker import Faker
from app import db
from models import Restaurant, Pizza, RestaurantPizza

fake = Faker()

def create_fake_restaurant():
    name = fake.company()
    address = fake.address()
    return Restaurant(name=name, address=address)

def create_fake_pizza():
    name = fake.word()
    ingredients = fake.sentence()
    return Pizza(name=name, ingredients=ingredients)

def create_fake_restaurant_pizza(restaurant, pizza):
    price = fake.random_int(min=1, max=30, step=1) 
    return RestaurantPizza(price=price, restaurant=restaurant, pizza=pizza)

def seed_fake_data(num_records):
    for _ in range(num_records):
        restaurant = create_fake_restaurant()
        pizza = create_fake_pizza()
        db.session.add(restaurant)
        db.session.add(pizza)
        db.session.add(create_fake_restaurant_pizza(restaurant, pizza))

    db.session.commit()

if __name__ == '__main__':
    seed_fake_data(10)  
