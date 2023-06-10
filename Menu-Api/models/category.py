from db import db

class Category(db.Model):
    __tablename__ = 'items_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    imageUrl = db.Column(db.Text)
    dishes = db.relationship('Dish',backref='category',lazy=True)

    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'imageUrl':self.imageUrl,
            'dishes': [dish.serialize() for dish in self.dishes]
        }