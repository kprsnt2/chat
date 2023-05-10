from fastapi import FastAPI,Request
# from pydantic import BaseModel
import uvicorn
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def read_root():
    return {"Hello": "Hello"}

if __name__ == "__main__":
    uvicorn.run("api:app",host='0.0.0.0', port=8080, reload=True)