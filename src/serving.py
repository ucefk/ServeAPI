import numpy as np
import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

from src.models import Sentiment


class Serving:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("out/", local_files_only=True)
        self.model = TFAutoModelForSequenceClassification.from_pretrained(
            "out/", local_files_only=True
        )

    def get_prediction(self, sentence):
        preprocessed_text = self.tokenizer(
            [sentence], return_tensors="np", padding=True
        )

        res = self.model.predict(dict(preprocessed_text))["logits"]
        probabilities = tf.nn.softmax(res)
        prediction = np.argmax(probabilities, axis=1)
        confidence = np.squeeze(probabilities)[prediction]

        return {
            "sentiment": "NEGATIVE" if int(prediction) == 0 else "POSITIVE",
            "confidence": round(float(confidence), 2),
        }
