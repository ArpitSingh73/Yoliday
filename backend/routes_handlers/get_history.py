import os
import psycopg2 
# connect to the PostgreSQL server
def get_chat_history(user_id):
    try:
        conn = psycopg2.connect(
            host=os.environ.get("POSTGRES_HOST"),
            dbname=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
            port=os.environ.get("POSTGRES_PORT"),
        )
        cur = conn.cursor()
        cur.execute("""SELECT casual_response, formal_response FROM user_chats WHERE user_id = %s""", (user_id,))
        prompts = cur.fetchall()
        cur.close()
        return prompts
    except Exception as error:
        print(f"problem while connecting to database: {error}")
        return {
            "success": False,
            "message": f"problem while connecting to database: ",
        }