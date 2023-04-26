# Create a TO DO list application that runs in terminal.
# It should allow user to log in. Each user should have his own tasks in to do list.
# User should be able to add/ update/ delete tasks.
# User information and task information should be kept in database


from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///todo.db")
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    tasks = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
