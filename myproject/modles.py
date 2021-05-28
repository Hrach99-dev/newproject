from myproject import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    phone = db.Column(db.Integer, unique=True, index=True)
    email = db.Column(db.String(128), unique=True, index=True)
    profile_image = db.Column(db.String(128), nullable=False, default='default_profile_image.png')
    password_hash = db.Column(db.String(128))

    products = db.relationship('Product', backref='author', lazy=True)

    def __init__(self, name, surname, phone, email, password) -> None:
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f'User - {self.name} {self.surname}'


class Product(db.Model, UserMixin):
    
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_name = db.Column(db.String(64), nullable=False)
    product_info = db.Column(db.Text, nullable=False)
    product_price = db.Column(db.String(64), nullable=False)
    # product_image = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, product_name, product_info, product_price, user_id) -> None:
        self.product_name = product_name
        self.product_info = product_info
        self.product_price = product_price
        self.user_id = user_id
    
    def __repr__(self) -> str:
        return f'Product {self.product_name} - Price: {self.product_price}'
        