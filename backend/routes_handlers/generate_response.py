from openai import OpenAI
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

load_dotenv(".env")


def generate_user_response(user_query: str, answer_type: str):
    try:
        print(f"Generating response for query: {user_query} with answer type: {answer_type}")
        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        model = genai.GenerativeModel(
            model_name=os.environ.get("GEMINI_MODEL"),
            system_instruction=f"""You are an Advanced AI capable of generating responses in different two different tones - formal and casual.\
                In formal tone, you should be more technical and precise.\
                In casual tone, you should be more friendly and approachable.\
                You have to return answer in JSON format with two keys - casual and formal.\
                do not use json word in response.\
                The user query is: {user_query}
                answer_type: {answer_type}""",
                generation_config={
                    "response_mime_type":"application/json"
                }
         )
        response = model.generate_content( user_query)
        response = json.loads(response.text)
        return response["casual"], response["formal"]
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response at this time."


# def generate_user_response(user_query: str, answer_type: str):
#     try:
#         # Call OpenAI's API to generate a response
#         print(f"Generating response for query: {user_query} with answer type: {answer_type}")
#         client = OpenAI(
#             api_key=os.environ.get("OPENAI_API_KEY")
#         )  # Replace with your OpenAI API key
#         prompt = f"""You are an Advanced AI capable of generating responses in different two different tones - formal and casual.\
#         In formal tone, you should be more technical and precise.\
#         In casual tone, you should be more friendly and approachable.\
#         You have to return answer in JSON format with two keys - casual and formal.\

#         The user query is: {user_query}
#         answer_type: {answer_type}"""

#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",  # Use the appropriate model name
#             messages=[
#                 {"role": "system", "content": prompt},
#                 {"role": "user", "content": user_query},
#             ],
#             response_format="json",
#             max_tokens=250,
#         )
#         response_text = response.choices[0].message.content
#         print(f"Response from OpenAI: {response_text}")
#         return ""
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return "Sorry, I couldn't generate a response at this time."
