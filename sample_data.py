import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO customers VALUES
(1,'Lokesh','lokesh@gmail.com','Chennai','2025-01-01'),
(2,'Arun','arun@gmail.com','Coimbatore','2025-02-01')
""")

cursor.execute("""
INSERT INTO products VALUES
(1,'Laptop','Electronics',50000),
(2,'Phone','Electronics',20000)
""")

cursor.execute("""
INSERT INTO orders VALUES
(1,1,1,2,'2025-05-10'),
(2,2,2,1,'2025-05-12')
""")

conn.commit()
conn.close()

print("Sample data inserted")