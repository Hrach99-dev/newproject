from flask import render_template, Blueprint


errorhandler = Blueprint('errorhandler', __name__)


@errorhandler.app_errorhandler(403)
def error403(e):
    return render_template('errorhandler/403.html'), 403

@errorhandler.app_errorhandler(404)
def error404(e):
    return render_template('errorhandler/404.html'), 404


@errorhandler.app_errorhandler(410)
def error410(e):
    return render_template('errorhandler/410.html'), 410


@errorhandler.app_errorhandler(500)
def error500(e):
    return render_template('errorhandler/500.html'), 500