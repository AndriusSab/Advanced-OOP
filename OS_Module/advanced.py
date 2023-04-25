import os

# print(os.name)

# print(os.getcwd())
# os.mkdir("OS_Module")
# creating new folder in directory

# with open("failas.txt", "w") as f: # write to txt file
#     f.write("Sveikas, pasauli!")

# with open("failas.txt", "a") as f:  # append to txt file
#     f.write("Sveikas, pasauli!")

# with open("failas.txt", "r+") as f:  # reads and lets to append to txt file
#     print(f.read())
#     f.write("Sveikas, pasauli2!")

# with open(
#     "failas.txt", "w", encoding="utf-8"
# ) as f:  # writes to txt file with lithuanian language syntax
#     print(f.read())
#     f.write("Sveikas, pasauli2!")

# with open(
#     "failas.txt", "r", encoding="utf-8"
# ) as f:  # reads from txt file with lithuanian language syntax
#     print(f.read())


# with open("failas2.txt", "w", encoding="utf-8") as f:
#     f.write("Čia yra pirmas sakinys \n")


# with open("failas2.txt", "a", encoding="utf-8") as f:
#     f.write("Čia yra antras sakinys \n")

# with open("failas.txt", 'r', encoding="utf-8") as failas:
#     print(failas.readlines())

# print(failas.read(100))

# # Čia yra devintas sakinys
# # Čia yra dešimtas sakinys

# with open("failas.txt", 'r') as r_failas:
#     with open("failo_kopija.txt", 'w') as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)

# with open("picture.jpg", "rb") as r_failas:
#     with open("picture_kopija.jpg", "wb") as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)

import pickle

a = 1024

with open("a.pkl", "wb") as pickle_out:
    pickle.dump(a, pickle_out)

with open("a.pkl", "rb") as pickle_in:
    naujas_a = pickle.load(pickle_in)

print(naujas_a)
