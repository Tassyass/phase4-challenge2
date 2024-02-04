# pizza_backend/pizzarestaurant/serializers.py

from flask_restful import fields

restaurant_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'address': fields.String,
}

pizza_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'ingredients': fields.String,
}

restaurant_pizza_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'ingredients': fields.String,
}
