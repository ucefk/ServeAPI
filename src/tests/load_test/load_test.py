import os
import random

from locust import HttpUser, between, task


def get_random_sentence():
    sentences = ["i don't know",
                 "i love you",
                 "i hate you"]
    return random.choice(sentences)


class ApiUser(HttpUser):
    wait_time = between(0.5, 1)

    def on_start(self):
        self.client.trust_env = True

    @task(1)
    def send_sentence(self):
        sentence = get_random_sentence()
        self.client.post("api/v1/inference/sentiment_analysis",
                         headers={
                                    'accept': 'application/json',
                                    'Content-Type': 'application/json'
                                },
                         json={'sentence': sentence})
