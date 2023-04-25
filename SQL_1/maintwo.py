import sqlite3

conn = sqlite3.connect("mydatabase.db")

# Create a new table called "lectures" with columns "name", "teacher", and "duration"
conn.execute("""CREATE TABLE lectures (name TEXT, teacher TEXT, duration INTEGER)""")

# Insert some data into the "lectures" table
conn.execute(
    "INSERT INTO lectures (name, teacher, duration) VALUES ('Vadyba', 'Domantas', 40)"
)
conn.execute(
    "INSERT INTO lectures (name, teacher, duration) VALUES ('Python', 'Donatas', 80)"
)
conn.execute(
    "INSERT INTO lectures (name, teacher, duration) VALUES ('Java', 'Tomas', 80)"
)

# Query the "lectures" table for records where the "duration" column is greater than 50
cursor = conn.execute("SELECT * FROM lectures WHERE duration > 50")
for row in cursor:
    print(row)

# Update the name of the lecture with the name "Python" to "Python programavimas"
conn.execute("UPDATE lectures SET name = 'Python programavimas' WHERE name = 'Python'")

# Delete the record where the teacher is "Tomas"
conn.execute("DELETE FROM lectures WHERE teacher = 'Tomas'")

# Query the "lectures" table and print out all the records
cursor = conn.execute("SELECT * FROM lectures")
for row in cursor:
    print(row)

# Commit the changes and close the database connection
conn.commit()
conn.close()
