from flask import Flask
from flask_login import LoginManager
from .models import db, User

myapp_obj = Flask(__name__)

myapp_obj.config['SECRET_KEY'] = 'your_secret_key_here'
myapp_obj.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
myapp_obj.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(myapp_obj)

login_manager = LoginManager()
login_manager.init_app(myapp_obj)
login_manager.login_view = 'login'  # Redirect here if @login_required fails

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app import routes
