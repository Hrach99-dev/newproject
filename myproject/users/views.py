from flask import flash, request, render_template, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from myproject import db
from myproject.modles import User, Product
from myproject.users.forms import LoginForm, RegisterForm, UpdateUserForm
from myproject.users.picture_handler import add_profile_pic


users = Blueprint('users', __name__)


@users.route('/registration', methods=['GET','POST'])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data,
                    surname=form.surname.data,
                    phone=form.phone.data,
                    email=form.email.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


@users.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
               next = url_for('core.index') 
            
            return redirect(next)
            
    return render_template('login.html', form=form)









@users.route('/logout')
def logout():

    logout_user()
    return redirect(url_for('core.index'))
