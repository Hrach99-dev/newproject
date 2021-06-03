from myproject.users.views import user_posts
from myproject.modles import Buyer, User, Product
from myproject import db


a = Buyer.query.all()
u = User.query.all()
p = Product.query.all()






for i in u:
    db.session.delete(i)
    db.session.commit()
db.session.commit()
print(u)