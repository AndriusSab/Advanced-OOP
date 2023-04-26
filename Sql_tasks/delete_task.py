from models import User, Task
from session import session

session.delete(task)
session.commit()
