from flask import render_template, url_for, abort,redirect, request, Blueprint, flash
from flask_login import current_user, login_required
from myproject import db
import myproject
from myproject.modles import Product
from myproject.product.forms import ProductForm
from myproject.product.product_picture_handler import add_product_pic

products = Blueprint('products', __name__)


@products.route('/add', methods=['GET','POST'])
@login_required
def add_product():
    
    form = ProductForm()
    if form.validate_on_submit():

        
        pic = None
        if form.product_picture.data:
            product_name = form.product_name + str(current_user.id)
            pic = add_product_pic(form.product_picture.data, product_name)
            

        my_product = Product(product_name=form.product_name.data,
                            product_info=form.product_info.data,
                            product_price=form.product_price.data,
                            user_id=current_user.id,
                            )
        
        my_product.product_image=pic

        db.session.add(my_product)
        db.session.commit()
        flash('Product Posted')
        return redirect(url_for('core.index'))
    return render_template('add_product.html', form=form)


@products.route('/<int:product_id>')
def product(product_id):
    my_product = Product.query.get_or_404(product_id)
    return render_template('product.html', my_product=my_product)



@products.route('/<int:product_id>/update', methods=['GET','POST'])
@login_required
def update_product(product_id):

    my_product = Product.query.get_or_404(product_id)
    if my_product.author != current_user:
        abort(403)

    form = ProductForm()
    if form.validate_on_submit():
        my_product.product_name = form.product_name.data
        my_product.product_info = form.product_info.data
        my_product.product_price = form.product_price.data  
        db.session.commit()
        flash('Product Updated')
        return redirect(url_for('products.product', product_id=my_product.id))

    elif request.method == 'GET':
        form.product_name.data = my_product.product_name
        form.product_info.data = my_product.product_info
        form.product_price.data = my_product.product_price
    return render_template('add_product.html', form=form)



@products.route('/<int:product_id>/delete', methods=['GET','POST'])
@login_required
def delete_product(product_id):

    my_product = Product.query.get_or_404(product_id)
    if my_product.author != current_user:
        abort(403)

    db.session.delete(my_product)
    db.session.commit()
    flash('Product Deleted')
    return redirect(url_for('core.index'))