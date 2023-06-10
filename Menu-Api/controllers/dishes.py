from flask import request
from flask_restful import Resource
from models.dish import Dish



class DishFilter(Resource):
    def get(self):
        category_id = request.args.get('category_id')
        if category_id is None:
            dishes = Dish.query.all()
        else:
            dishes = Dish.query.filter_by(category_id=category_id).all()
        return [dish.serialize() for dish in dishes]