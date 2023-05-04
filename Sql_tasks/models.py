# Create a TO DO list application that runs in terminal.
# It should allow user to log in. Each user should have his own tasks in to do list.
# User should be able to add/ update/ delete tasks.
# User information and task information should be kept in database


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):  # type: ignore
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column("Username", String, unique=True, nullable=False)
    email = Column("Email", String, unique=True, nullable=False)
    password = Column("Password", String, nullable=False)
    tasks = relationship("Task", back_populates="users")


class Task(Base):  # type: ignore
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    user_id = Column("User ID", Integer, ForeignKey("users.id"))
    deadline_time = Column("Deadline", DateTime)
    description = Column("Description", String, nullable=False)
    users = relationship("User", back_populates="tasks")
