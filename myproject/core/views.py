from flask import render_template, Blueprint


core = Blueprint('core', __name__)


@core.route('/')
@core.route('/home')
def index():
    return render_template('index.html')

@core.route('/about')
def about():
    return render_template('about.html')