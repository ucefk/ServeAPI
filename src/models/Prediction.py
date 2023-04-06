from pydantic import BaseModel

from src.models.Sentiment import Sentiment


class Prediction(BaseModel):
    """
    Prediction data model.
    """

    sentiment: Sentiment
    confidence: float
