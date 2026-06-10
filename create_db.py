import sqlite3

conn = sqlite3.connect("database.db")

with open("schema.sql", "r") as file:
    conn.executescript(file.read())

conn.commit()
conn.close()

print("Database initialized")