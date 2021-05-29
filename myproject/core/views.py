import myproject
from flask import render_template, Blueprint, request
from myproject.modles import Product


core = Blueprint('core', __name__)


@core.route('/')
@core.route('/home')
def index():
    page = request.args.get('page',1,type=int)
    product_posts = Product.query.order_by(Product.date.desc()).paginate(page=page,per_page=5)
    return render_template('index.html', product_posts=product_posts)

@core.route('/about')
def about():
    return render_template('about.html')