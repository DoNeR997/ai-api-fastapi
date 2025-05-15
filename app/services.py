import httpx
from app.config import OPENAI_API_KEY
from fastapi import HTTPException

async def ask_openai(question: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 429:
            raise HTTPException(status_code=429, detail="Za dużo zapytań – spróbuj ponownie za chwilę.")
        elif e.response.status_code == 401:
            raise HTTPException(status_code=401, detail="Nieprawidłowy klucz API OpenAI.")
        else:
            raise HTTPException(status_code=500, detail=f"Błąd OpenAI: {e.response.text}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Błąd wewnętrzny: {str(e)}")
