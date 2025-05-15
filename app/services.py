import httpx
from app.config import OPENAI_API_KEY
from fastapi import HTTPException

async def ask_openai(question: str) -> str:
    # Jeśli klucz nie istnieje lub nadal placeholder
    if not OPENAI_API_KEY or OPENAI_API_KEY == "tu_wklej_swoj_klucz":
        return "This would be the AI's response if the API were active and paid."

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
        if e.response.status_code in [401, 429]:
            # Jeśli brak autoryzacji lub limit – pokaż demo odpowiedź
            return "This would be the AI's response if the API were active and paid."
        else:
            raise HTTPException(status_code=500, detail=f"OpenAI error: {e.response.text}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
