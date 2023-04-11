# Write a function that calculates difference in days between two datetimes.
# Write a function that takes a datetime object, which will represent employees starting work day. and will return amount of total holidays gained during the work until today. 1 Month = 1.6 day off
# find next 3 Fridays that happend to be Friday the 13th (classic)
# Write a python function that takes nothing but returns the datetime object of last Friday
# Write a Python program to get the last day of a specified year and month, Example: Monday, Tuesday etc.

# import datetime


# def time_diff_days(datetime1, datetime2):
#     datetime1 = datetime.datetime()
#     datetime2 = datetime.datetime()

#     return datetime1 - datetime2


# datetime1 = datetime.datetime(2020, 10, 25)
# datetime2 = datetime.datetime(2020, 10, 15)

# diference = time_diff_days(datetime1, datetime2)

# print(diference)


# import datetime


# def days_off(starting_day: datetime.datetime) -> float:
#     current_day = datetime.datetime.now()
#     diff = current_day - starting_day
#     return diff.days * 1.6


# starting_day = datetime.datetime(2023, 4, 10)
# print(days_off(starting_day))


# Write a terminal program that required user to login.
# If user does not have an account he should register. credentials are username and password. Store the information in the file txt or pickle. Validate user credentials from the file.
# # Once user has logged in: print text: "Hello, <username>".
# import os

# user_name = "Andrius"
# user_password = "password"

# while True:
#     try:
#         print("Hello, please LOGIN")
#         name_input = input("Please enter username: ")
#         pass_input = input("Please enter password: ")

#         if name_input == user_name and pass_input == user_password:
#             print(f"Hi {user_name}")
#             break
#         else:
#             print("Incorrect login information.")
#             break
#     except Exception
# print("To create new account please enter your name and password")


# with open("failas.txt", "w") as f: # write to txt file
#     f.write("Sveikas, pasauli!")

# with open("failas.txt", "a") as f:  # append to txt file
#     f.write("Sveikas, pasauli!")


import pickle
import os

# Define the name of the file to store the user information
USER_FILE = "users.pkl"

class Login:

def __init__(self, username:str, password:str) ->:None
    self.username = username
    self.password = password

def register():
    """
    Register a new user by prompting for a username and password.
    """
    
    # Check if the username already exists
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "rb") as f:
            users = pickle.load(f)
        if username in users:
            print("Username already exists")
            return

    # Add the new user to the dictionary of users
    with open(USER_FILE, "ab") as f:
        if os.path.getsize(USER_FILE) == 0:
            users = {}
        else:
            with open(USER_FILE, "rb") as f:
                users = pickle.load(f)
        users[username] = password
        pickle.dump(users, f)

    print("User registered successfully")


def login():
    """
    Prompt for a username and password and check if they are valid.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Load the dictionary of users from the file
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "rb") as f:
            users = pickle.load(f)

        # Check if the username and password match a user in the dictionary
        if username in users and users[username] == password:
            print(f"Hello, {username}")
        else:
            print("Invalid username or password")
    else:
        print("No users registered yet")


# Main loop
username = input("Enter a username: ")
password = input("Enter a password: ")

while True:
    action = input("Enter 'login' to login or 'register' to register: ")
    if action == "register":
  =
        login()
    else:
        print("Invalid action")



import pickle
import os

# Define the name of the file to store the user information
USER_FILE = "users.pkl"

class Login:
    def __init__(self, username:str, password:str) -> None:
        self.username = username
        self.password = password

def register(users, username:str, password:str):
    """
    Register a new user by prompting for a username and password.
    """
    
    # Check if the username already exists
    if username in users:
        print("Username already exists")
        return

    # Add the new user to the dictionary of users
    users[username] = password

    # Save the updated user dictionary to the file
    with open(USER_FILE, "wb") as f:
        pickle.dump(users, f)

    print("User registered successfully")


def login(users):
    """
    Prompt for a username and password and check if they are valid.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match a user in the dictionary
    if username in users and users[username] == password:
        print(f"Hello, {username}")
    else:
        print("Invalid username or password")


# Main program
while True:
    # Prompt the user to enter a username and password
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Load the dictionary of users from the file, if it exists
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "rb") as f:
            users = pickle.load(f)
    else:
        users = {}

    action = input("Enter 'login' to login or 'register' to register: ")

    if action == "register":
        register(users, username, password)
    elif action == "login":
        login(users)
    else:
        print("Invalid action")