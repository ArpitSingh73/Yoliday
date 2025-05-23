import uuid
import os
import psycopg2
from datetime import datetime


def save_to_db(casual_resp: str, formal_resp: str, user_id: str, query: str):
    try:    
        print("Saving data to PostgreSQL...")
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
        casual_response = str(casual_resp)
        formal_response = str(formal_resp)
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
        print("Data saved to PostgreSQL successfully.")
    except Exception as e:
        print(" Error occured while save data to postgres -- ", e)
    