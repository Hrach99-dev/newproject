import myproject
from flask import render_template, Blueprint, request
from myproject.modles import Product


core = Blueprint('core', __name__)


@core.route('/')
@core.route('/home')
def index():
    
    product_posts = Product.query.order_by(Product.date.desc())
    return render_template('index.html', product_posts=product_posts)

@core.route('/about')
def about():
    return render_template('about.html')