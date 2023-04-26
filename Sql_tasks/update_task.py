from models import User, Task
from session import session

# Create a new task
new_task = Task(task="Create something beautiful")

# Get the user you want to associate the task with
user = session.query(User).get(1)  # Assuming the user with ID 1 exists in the database

# Associate the task with the user
new_task.user = user

# Add the task to the session and commit the changes
session.add(new_task)
session.commit()
