from flask_restful import Resource
from models.category import Category

class CategoriesAll(Resource):
    def get(self):
        categories = Category.query.all()
        return [category.serialize() for category in categories]