from models import User, Task
from session import session

user = session.query(User).get(1)

new_task = Task(description="Clean room", user=user)

session.add(new_task)
session.commit()
