import json
from datetime import datetime

def log_query(question, sql):

    try:
        with open("query_logs.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append({
        "timestamp": str(datetime.now()),
        "question": question,
        "sql": sql
    })

    with open("query_logs.json", "w") as f:
        json.dump(logs, f, indent=4)