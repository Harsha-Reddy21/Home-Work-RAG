

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict, List, Any, Optional
import os
from dotenv import load_dotenv
import json
import numpy as np

from src.llm_chain import get_evulate_function, feedback_function
from src.retrieval import retrieve_similar_examples

app=FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/generate-code")
async def generate_validation(activity: str):
    pass



@app.post("/feedback-answer")
async def validate_answer(answer: str):
    return {"status": "ok"}






if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)