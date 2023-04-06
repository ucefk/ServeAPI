from pydantic import BaseModel


class InferenceInput(BaseModel):
    sentence: str
