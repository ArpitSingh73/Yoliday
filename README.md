# AI Response Generator

This project is an AI-powered response generator with a Streamlit frontend and a FastAPI backend. It generates responses in both formal and casual tones and stores user queries and responses in a PostgreSQL database.

## Project Structure

```
backend/
    app.py
    routes_handlers/
        generate_response.py
        get_history.py
    utils/
        postgres_uitls.py
    .env
frontend/
    home.py
```

## Features

- Generate AI responses in formal and casual tones.
- Store and retrieve user queries and responses.
- View query history per user.

## Setup

### Prerequisites

- Python 3.10+
- PostgreSQL database
- [OpenAI](https://platform.openai.com/) and/or [Google Gemini](https://ai.google.dev/) API keys

### Backend

1. Install dependencies:
    ```sh
    pip install fastapi uvicorn psycopg2-binary python-dotenv openai google-generativeai
    ```

2. Create a `.env` file in the `backend/` directory with the following variables:
    ```
    POSTGRES_HOST=your_postgres_host
    POSTGRES_DB=your_db_name
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_PORT=5432
    GEMINI_API_KEY=your_gemini_api_key
    GEMINI_MODEL=your_gemini_model_name
    OPENAI_API_KEY=your_openai_api_key
    ```

3. Start the backend server:
    ```sh
    uvicorn app:app --reload
    ```

### Frontend

1. Install dependencies:
    ```sh
    pip install streamlit requests python-dotenv
    ```

2. Run the Streamlit app:
    ```sh
    streamlit run home.py
    ```

## Usage

- Open the Streamlit app in your browser.
- Enter your query, select the tone, and provide your user ID.
- Click "Generate" to receive AI-generated responses.
- View your query history in the sidebar.

## License

This project is for educational purposes.
