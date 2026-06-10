import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_sql(question):

    prompt = f"""
    You are an SQLite expert.

    Database Schema:

    customers(id,name,email,city,created_at)
    products(id,name,category,price)
    orders(id,customer_id,product_id,quantity,order_date)

    Rules:
    - Return ONLY valid SQLite SQL
    - Only SELECT queries are allowed
    - Never use INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE
    - Always use meaningful aliases
    - Do not use markdown
    - Do not use ```sql
    - If the user asks to modify, delete, update, insert, drop, truncate, or alter data, return exactly:
    UNSAFE_QUERY
    
    Question:
    {question}
    """

    response = model.generate_content(prompt)

    sql = response.text.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()

def explain_results(question, results):

    prompt = f"""
    User Question:
    {question}

    Query Results:
    {results}

    Give a concise business summary in 2-3 sentences.

    Do not list every row.
    Focus on key insights.
    """

    response = model.generate_content(prompt)

    return response.text.strip()