import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'msk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'




from myproject.core.views import core
from myproject.error_pages.errorhandler import errorhandler
from myproject.users.views import users
from myproject.product.views import products


app.register_blueprint(core)
app.register_blueprint(errorhandler)
app.register_blueprint(users)
app.register_blueprint(products)