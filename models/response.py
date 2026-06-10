from pydantic import BaseModel

class QueryResponse(BaseModel):
    sql: str
    results: list
    explanation: str