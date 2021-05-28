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


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():

    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.name + current_user.surname
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic
        
        current_user.name = form.name.data
        current_user.surname = form.surname.data
        current_user.phone = form.phone.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.name.data = current_user.name
        form.surname.data = current_user.surname
        form.phone.data = current_user.phone
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)


@users.route("/<email>")
def user_posts(email):
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(email=email).first_or_404()
    product_posts = Product.query.filter_by(author=user).order_by(Product.date.desc()).paginate(page=page,per_page=5)
    return render_template('user_product_posts.html', product_posts=product_posts, user=user)