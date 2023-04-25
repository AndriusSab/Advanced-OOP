# import sqlite3

# conn = sqlite3.connect("mydb.db")
# c = conn.cursor()

# with conn:
#     c.execute(
#         """CREATE TABLE IF NOT EXISTS
#     darbuotojai (
#     vardas text,
#     pavarde text,
#     atlyginimas integer
#     )"""
#     )

# conn.commit()
# conn.close()

# with conn:
#     c.execute("INSERT INTO darbuotojai VALUES ('Domantas', 'Rutkauskas', 1500)")

#     c.execute("INSERT INTO darbuotojai VALUES ('Rimas', 'Radzevičius', 1000)")


import sqlite3

conn = sqlite3.connect("duomenu_baze.db")
c = conn.cursor()

with conn:
    c.execute(
        """CREATE TABLE IF NOT EXISTS
    darbuotojai (
    vardas text,
    pavarde text,
    atlyginimas integer
    )"""
    )

while True:
    print("Įveskite darbuotoją")
    vardas = input("Vardas: ")
    pavarde = input("Pavarde:")
    atlyginimas = int(input("atlyginimas :"))

    with conn:
        c.execute(
            f"INSERT INTO darbuotojai VALUES ('{vardas}', '{pavarde}', {atlyginimas})"
        )

    with conn:
        c.execute("SELECT * FROM darbuotojai")
        print(c.fetchall())
