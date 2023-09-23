from flask import Flask, request, jsonify
from .models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)

