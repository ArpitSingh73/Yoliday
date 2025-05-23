import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")


def call_generate_api(query, tone, user_id):
    payload = {"query": query, "tone": tone, "user_id": user_id}
    print(payload)
    try:
        # GENERATE_API_URL = os.environ.get("GENERATE_API_URL")
        # print(GENERATE_API_URL)
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            "http://127.0.0.1:8000/generate", json=payload, timeout=30, headers=headers
        )
        response.raise_for_status()
        data = response.json()
        print(data)
        return data.get("casual_response", ""), data.get("formal_response", "")
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}", ""

def call_history_api(user_id):
    try:
        # HISTORY_API_URL = os.environ.get("HISTORY_API_URL")
        # print(HISTORY_API_URL)
        response = requests.get("http://127.0.0.1:8000/history", params={"user_id": user_id})
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}", ""

st.title("AI Response Generator")

tone = st.selectbox(
            "Select Tone/Style", [ "Formal", "Casual" ]
        )
user_input = st.text_input("Enter your query here:")

user_id = st.text_input("Enter your user ID:")

if tone and user_id and user_input:
    if st.button("Generate"):
        response1, response2 = call_generate_api(user_input, tone, user_id)
        st.subheader("Casual Response ")
        st.write(response1)
        st.subheader("Formal Response ")
        st.write(response2)
    
        # Display the query history
        with st.sidebar.expander("Query History", expanded=True):
            st.write("This is the query history section.")
            history = call_history_api(user_id)
            for i, (response1, response2) in enumerate(history, start=1):
                st.write(f"Casual Response: {response1}")
                st.write(f"Formal Response: {response2}")
                st.write("---")
