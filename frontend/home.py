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


# history = [
#     { "query": "Explain blockchain", "response1": "Here's a simple explanation of blockchain...", "response2": "A blockchain is a distributed ledger technology..."},
#     {  "query": "What is AI?", "response1": "AI is the simulation of human intelligence in machines.", "response2": "Artificial Intelligence refers to the capability of a machine to imitate intelligent human behavior."},
#     {  "query": "What is Python?", "response1": "Python is a high-level programming language.", "response2": "Python is an interpreted, high-level, general-purpose programming language."},
#     ]


# Here you can implement the logic to fetch and display the history of queries and responses


st.title("AI Response Generator")

tone = st.selectbox(
            "Select Tone/Style", [ "Formal", "Casual" ]
        )
user_input = st.text_input("Enter your query here:")

user_id = st.text_input("Enter your user ID:")

if st.button("Generate"):
    response1, response2 = call_generate_api(user_input, tone, user_id)
    st.subheader("AI Response 1")
    st.write(response1)
    st.subheader("AI Response 2")
    st.write(response2)
    # history.append({"query": user_input, "response1": response1, "response2": response2})

    # Display the query history
    with st.sidebar.expander("Query History", expanded=True):
        st.write("This is the query history section.")
        history = call_history_api(user_id)
        print(history)
        for i, (response1, response2) in enumerate(history, start=1):
            st.write(f"Response 1: {response1}")
            st.write(f"Response 2: {response2}")
            st.write("---")
