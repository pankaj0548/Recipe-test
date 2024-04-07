from flask import Flask
from app.views import blueprints, login_manager
from app.db.models import User
from app.modules.my_sql import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ygae@1!ffsyud@g&*ch%$avplz/d/615r&2vi21sgf(3fh*hu.x'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/recipes'
    
    for i in blueprints:
        app.register_blueprint(i)
    
    login_manager.init_app(app)
    db.init_app(app)
        
    @login_manager.user_loader
    def load_user(email):
        user = User.query.filter_by(email=email).first()
        if user:
            return user
        return None
    
    def create_db():
        with app.app_context():
            db.create_all()
    create_db()
    return app