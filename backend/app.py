import uuid
import os
import psycopg2
from datetime import datetime
from fastapi import FastAPI
from fastapi import Form, Body
from dotenv import load_dotenv
from routes_handlers.get_history import get_chat_history
from routes_handlers.generate_response import generate_user_response
load_dotenv(".env")


# FastAPI app
app = FastAPI()


# Dummy response generator (replace with real AI logic)
def generate_responses(query: str):
    casual = f"Sure! Here's a simple take: {query}"
    formal = f"Certainly. Here is a formal explanation: {query}"
    return casual, formal


@app.post("/generate")
def generate(
    query: str = Body(...),
    tone: str = Body(...),
    user_id: str = Body(...)
):
    try:
        # casual, formal = generate_responses(query)
        casual, formal = generate_user_response(query, tone)
        conn = psycopg2.connect(
            host=os.environ.get("POSTGRES_HOST"),
            dbname= os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
            port=os.environ.get("POSTGRES_PORT"),
             
        )
        cur = conn.cursor()
        id = uuid.uuid4()
        query = str(query)
        casual_response = str(casual)
        formal_response = str(formal)
        created_at = datetime.now()

        insert_query = """
            INSERT INTO user_chats (id, user_id, query, casual_response, formal_response, created_at)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(
            insert_query,
            (str(id), user_id, query, casual_response, formal_response, created_at),
        )
        conn.commit()
        cur.close()
        print("Data inserted successfully")

        return {"casual_response": casual, "formal_response": formal}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": "An error occurred while generating responses."} 


@app.get("/history")
def get_history(user_id: str):

    try:
        return get_chat_history(user_id)
    except Exception as error:
        print(f"problem while connecting to database: {error}")
        return {
            "success": False,
            "message": f"problem while connecting to database: ",
        }

    # Creating a cursor with name cur.
