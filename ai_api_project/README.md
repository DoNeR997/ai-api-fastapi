# AI Question API (FastAPI + OpenAI) – Demo Version

This project is a simple REST API built with Python and FastAPI that simulates asking questions to an AI assistant (OpenAI GPT-3.5-turbo model).

## 🔧 Features

- `/ask` endpoint that receives a question and returns a (simulated) AI answer
- Data validation with Pydantic
- Proper error handling and HTTP response codes
- Interactive API documentation at `/docs` (Swagger UI)
- Environment variable management using `.env`

## 💡 Why is the answer simulated?

OpenAI API requires a paid API key (separate from ChatGPT Plus).  
This project focuses on backend structure and integration logic, but:

**Instead of real OpenAI requests, it returns a mock answer:**

> `"This would be the AI's response if the API were active and paid."`

## 🚀 Possible Extensions (Free Alternatives)

This project can be upgraded or made fully functional using free APIs such as:

- **OpenRouter.ai** – free proxy access to multiple LLMs (including OpenAI-compatible)
- **Gemini API (Google AI)** – free with a Google account
- **HuggingFace API** – free models available with API tokens

## 🛠️ Technologies Used

- Python 3
- FastAPI
- Pydantic
- httpx
- dotenv
- Git + GitHub

## 🧪 How to Run Locally

1. Create a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. (Optional) Create a `.env` file:
    ```
    OPENAI_API_KEY=your_key_here
    ```

4. Start the app:
    ```bash
    uvicorn app.main:app --reload
    ```

5. Open the browser:
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

✅ Clean structure, mock integration with real-world APIs, ready for further development or deployment.

