

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



app=FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/generate-validation")
async def generate_validation(activity: str):
    return {"status": "ok"}


@app.post("/validate-answer")
async def validate_answer(answer: str):
    return {"status": "ok"}


@app.post("/test-validation")
async def test_validation(test_cases: list[str]):
    return {"status": "ok"}



@app.post("/improve-prompts")
async def improve_prompts(prompt: str):
    return {"status": "ok"}




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)