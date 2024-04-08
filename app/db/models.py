from flask_login import UserMixin
from app.modules.my_sql import db
from sqlalchemy.orm import relationship

class User(UserMixin, db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50),  nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    recipes = relationship('Recipe', backref='author', lazy=True)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def is_authenticated(self):
        return True
    
    def get_id(self):
        return self.email

class Recipe(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    image = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    created_by = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def update(self):
        db.session.add(self)
        db.session.flush()
        db.session.commit()
