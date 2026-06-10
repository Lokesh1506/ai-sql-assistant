import sqlite3

def execute_query(sql):

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]