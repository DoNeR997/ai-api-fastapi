from fastapi import FastAPI
from app.services import ask_openai
from app.schemas import QuestionRequest, QuestionResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API działa!"}

@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    answer = await ask_openai(request.question)
    return {"answer": answer}
