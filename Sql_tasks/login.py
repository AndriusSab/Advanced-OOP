from session_module import SqliteDatabase
from models import User, Task


def welcome() -> None:
    print("Welcome to the task manager!")


def first_input_selection() -> int:
    while True:
        try:
            valide_inputs = [1, 2, 3]
            selection = int(
                input(
                    "Select your action: \n1. Register new user \n2. Log in \n3. Exit\n"
                )
            )
            if selection in valide_inputs:
                return selection
        except ValueError:
            print("You have to input numer between 1 and 3!")
            continue


def second_input_selection() -> int:
    while True:
        try:
            valide_inputs = [1, 2, 3, 4, 5, 6]
            selection = int(
                input(
                    "Select your action: \n1. Create new task \n2. Update task \n3. Delete task \n4. Get all tasks \n5. Log out \n6. Exit\n"
                )
            )
            if selection in valide_inputs:
                return selection
        except ValueError:
            print("You have to input numer between 1 and 6!")
            continue
