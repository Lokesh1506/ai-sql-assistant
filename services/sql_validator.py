FORBIDDEN = [
    "DELETE",
    "UPDATE",
    "INSERT",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "ATTACH"
]

def is_safe(sql: str):

    sql_upper = sql.upper()

    for keyword in FORBIDDEN:
        if keyword in sql_upper:
            return False

    return sql_upper.strip().startswith("SELECT")