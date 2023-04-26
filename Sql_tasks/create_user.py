from models import User
from session import session

new_user = User(username="Andrius", password="123456")
session.add(new_user)
session.commit()
