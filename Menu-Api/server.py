from flask import Flask
from db import db
from flask_restful import Api
from flask_cors import CORS
from controllers.categories import CategoriesAll
from controllers.dishes import DishFilter
from config import DBUSER,DBPASS,DBHOST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}/postgres'
app.config['SECRET_KEY'] = 'sadkjfsakgjdahgreaua56465oijadsfl2helloman'
db.init_app(app)
api = Api(app)
CORS(app)

with app.app_context():
    db.create_all()
    
api.add_resource(CategoriesAll,'/categories')
api.add_resource(DishFilter,'/dishes')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')