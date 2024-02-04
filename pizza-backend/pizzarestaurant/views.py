# pizza_backend/pizzarestaurant/views.py
# pizza_backend/pizzarestaurant/views.py

from flask_restful import Resource, reqparse, abort, marshal
from .models import db, Restaurant, Pizza, RestaurantPizza
from .serializers import restaurant_fields, pizza_fields, restaurant_pizza_fields


class RestaurantListResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        return {'restaurants': [marshal(restaurant, restaurant_fields) for restaurant in restaurants]}

class RestaurantResource(Resource):
    def get(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant is None:
            abort(404, error="Restaurant not found")
        
        pizzas = Pizza.query.join(RestaurantPizza).filter(RestaurantPizza.restaurant_id == restaurant_id).all()
        restaurant_data = marshal(restaurant, restaurant_fields)
        restaurant_data['pizzas'] = [marshal(pizza, pizza_fields) for pizza in pizzas]
        return {'restaurant': restaurant_data}

    def delete(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant is None:
            abort(404, error="Restaurant not found")

        restaurant_pizzas = RestaurantPizza.query.filter_by(restaurant_id=restaurant_id).all()
        for rp in restaurant_pizzas:
            db.session.delete(rp)

        db.session.delete(restaurant)
        db.session.commit()
        return '', 204

class PizzaListResource(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        return {'pizzas': [marshal(pizza, pizza_fields) for pizza in pizzas]}

class RestaurantPizzaCreateResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('pizza_id', type=int, required=True)
        parser.add_argument('restaurant_id', type=int, required=True)
        args = parser.parse_args()

        pizza = Pizza.query.get(args['pizza_id'])
        restaurant = Restaurant.query.get(args['restaurant_id'])

        if pizza is None or restaurant is None:
            abort(400, error="Invalid pizza_id or restaurant_id")

        new_pizza = RestaurantPizza(price=args['price'], pizza=pizza, restaurant=restaurant)
        db.session.add(new_pizza)
        db.session.commit()

        return {'pizza': marshal(pizza, pizza_fields)}
