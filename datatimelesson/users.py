import pickle


users_list = {"Andrius": "labas", "Saulius": "belekas"}


users = open("dict.users", "wb")
pickle.dump(users_list, users)
users.close()


# import pickle

# example_dict = {1: "6", 2: "2", 3: "f"}

# pickle_out = open("dict.pickle", "wb")
# pickle.dump(example_dict, pickle_out)
# pickle_out.close()
