import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/generate"   


def call_backend_api(query, tone):
    payload = {"query": query, "tone": tone}
    try:
        # response = requests.post(API_URL, json=payload, timeout=30)
        # response.raise_for_status()
        # data = response.json()
        # return data.get("response1", ""), data.get("response2", "")
        return "Casual response", "Formal response"
    except Exception as e:
        return f"Error: {e}", ""


st.title("AI Response Generator")

tone = st.selectbox(
        "Select Tone/Style", ["Neutral", "Formal", "Casual", "Humorous"]
    )
user_input = st.text_input("Enter your query here:")

if st.button("Generate"):
        response1, response2 = call_backend_api(user_input, tone)
        st.subheader("AI Response 1")
        st.write(response1)
        st.subheader("AI Response 2")
        st.write(response2)
 