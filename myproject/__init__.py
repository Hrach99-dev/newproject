from flask import Flask



app = Flask(__name__)


from myproject.core.views import core
from myproject.error_pages.errorhandler import errorhandler

app.register_blueprint(core)
app.register_blueprint(errorhandler)