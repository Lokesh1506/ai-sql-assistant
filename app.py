from fastapi import FastAPI
from pydantic import BaseModel

from services.llm_service import generate_sql, explain_results
from services.db_service import execute_query
from services.sql_validator import is_safe
from services.log_service import log_query

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query(request: QueryRequest):

    try:

        sql = generate_sql(request.question)

        if sql == "UNSAFE_QUERY":
            return {
                "error": "Unsafe query detected"
            }

        log_query(
            request.question,
            sql
        )
        
        if not is_safe(sql):
            return {
                "error": "Unsafe query detected"
            }

        results = execute_query(sql)

        explanation = explain_results(
            request.question,
            results
        )

        return {
            "sql": sql,
            "results": results,
            "explanation": explanation
        }

    except Exception as e:

        return {
            "error": "Unable to process request. Please try again later."
        }
    
@app.get("/")
def home():
    return {
        "application": "AI SQL Assistant",
        "status": "Running"
    }