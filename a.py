from myproject.modles import Buyer, User
from myproject import db

user = User.query.filter_by(name='Gal').first()
a = Buyer.query.filter_by(user_id=user.id)

for i in a:
    print(i)







# for i in a:
#     db.session.delete(i)
#     db.session.commit()
# db.session.commit()