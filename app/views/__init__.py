from os import listdir, path
from importlib import import_module
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

blueprints = [import_module(f"app.views.{i[:-3]}").bp for i in listdir(path.dirname(__file__)) if i.endswith(".py") and i != "__init__.py"]