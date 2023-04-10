import uvicorn
from fastapi import FastAPI

from src.models import InferenceInput, Prediction
from src.serving import Serving

app = FastAPI(
    title="ServeAPI",
    description="API for a prediction service",
)

serving = Serving()


@app.post(
    path="/v1/inference/sentiment_analysis",
    response_model=Prediction,
    tags=["Sentiment Analysis"],
    summary="Post a sentiment analysis prediction",
    description="Post a sentiment analysis prediction",
)
async def get_sentiment_analysis(inference_input: InferenceInput) -> Prediction:
    return Prediction(**serving.get_prediction(sentence=inference_input.sentence))


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", reload=True)
