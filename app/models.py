from . import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    bedrooms = db.Column(db.Float, nullable=False)
    bathrooms = db.Column(db.Float, nullable=False)
    photo = db.Column(db.String(200), nullable=False)
