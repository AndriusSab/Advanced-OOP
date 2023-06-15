
from app import db, Message, app

with app.app_context():

jonas = Message.query.get(Message,1)
db.session.delete(jonas)
db.session.commit()
print(Message.query.all())
