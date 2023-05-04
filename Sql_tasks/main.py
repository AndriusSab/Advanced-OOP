from session_module import SqliteDatabase
from datetime import datetime
from models import User, Task, Base
from login import first_input_selection, second_input_selection
import getpass
import sys


tm = SqliteDatabase("Task_manager.db", Base)
tm.create_database()

while True:
    selection = first_input_selection()

    if selection == 1:
        username = input("Please enter your username:\n")
        email = input("Please enter your email\n")
        password = getpass.getpass("Please enter your password:\n")
        tm.create_user(username=username, email=email, password=password)

    if selection == 2:
        username = input("Please enter your username:\n")
        password = getpass.getpass("Please enter your password:\n")
        if tm.authenticate_user(name=username, password=password):
            print("Access granted")
            user = tm.get_user(name=username)
            while True:
                second_selection = second_input_selection()

                if second_selection == 1:
                    task_date_time = datetime.strptime(
                        input("Enter the end date of the task (YYYY-MM-DD HH:MM):\n"),
                        "%Y-%m-%d %H:%M",
                    )
                    task_description = input("Enter the description of the task:\n")
                    tm.create_task(
                        user=user,
                        task_date_time=task_date_time,
                        task_description=task_description,
                    )

                if second_selection == 2:
                    tm.get_objects_by_username(username)
                    task_id = int(input("Input ID of task you want to update:\n"))
                    updating_task = tm.get_task(task_id)
                    while True:
                        column = int(
                            input(
                                "select column, you want to update: \n1. Date \n2. Description \n3. Back\n"
                            )
                        )
                        if column == 1:
                            updating_task.end_date_time = datetime.strptime(
                                input(
                                    "Update the end date of the task (YYYY-MM-DD HH:MM):\n"
                                ),
                                "%Y-%m-%d %H:%M",
                            )
                            tm.update_object(updating_task)

                        if column == 2:
                            updating_task.description = input(
                                "Update the description of the task:\n"
                            )
                            tm.update_object(updating_task)

                        if column == 3:
                            break

                if second_selection == 3:
                    tm.get_objects_by_username(username)
                    task_id = int(input("Input ID of task you want to delete:\n"))
                    deleting_task = tm.get_task(task_id)
                    tm.delete_object(deleting_task)

                if second_selection == 4:
                    tm.get_objects_by_username(username)

                if second_selection == 5:
                    break

                if second_selection == 6:
                    sys.exit("Task manager closed")

    if selection == 3:
        sys.exit("Task manager closed")
