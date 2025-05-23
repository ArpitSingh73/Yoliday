from fastapi import FastAPI
from fastapi import Body
from dotenv import load_dotenv
from routes_handlers.get_history import get_chat_history
from routes_handlers.generate_response import generate_user_response
from utils.postgres_uitls import save_to_db
load_dotenv(".env")

# FastAPI app
app = FastAPI()

@app.post("/generate")
def generate(query: str = Body(...), tone: str = Body(...), user_id: str = Body(...)):
    try:
        # casual, formal = generate_responses(query)
        casual_resp, formal_resp = generate_user_response(query, tone)

        save_to_db(casual_resp, formal_resp, user_id, query)

        print("Data inserted successfully")
        return {"casual_response": casual_resp, "formal_response": formal_resp}
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
