# pizza_backend/pizzarestaurant/urls.py

from flask import Blueprint
from flask_restful import Api
from .views import RestaurantListResource, RestaurantResource, PizzaListResource, RestaurantPizzaCreateResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(RestaurantListResource, '/restaurants')
api.add_resource(RestaurantResource, '/restaurants/<int:restaurant_id>')
api.add_resource(PizzaListResource, '/pizzas')
api.add_resource(RestaurantPizzaCreateResource, '/restaurant_pizzas')
