# app.py
from fastapi import FastAPI, APIRouter
import uvicorn
from classifier import Classifier
from model import Model
from nlp import sentiment_analysis
import logging

logging.basicConfig(level = logging.INFO)


app = FastAPI()
router = APIRouter()
classifier = Classifier()


@router.get("/")
async def home():
  return {"message": "Machine Learning service"}

@router.post("/sentiment")
async def data(data: dict):
  try:
    input_text = data["text"]
    res = sentiment_analysis(classifier, input_text)
    return res
  except Exception as e:
    logging.error("Something went wrong")

app.include_router(router)

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("app:app", reload=True, port=6000, host="0.0.0.0")