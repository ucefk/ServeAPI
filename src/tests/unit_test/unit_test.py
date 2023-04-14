import json

import pytest


def test_positive_sentiment(client):
    data = {
        'sentence': 'I love you'
    }
    response = client.post('/inference/sentiment_analysis', json=data)
    assert response.status_code == 200
    response_data = json.loads(response.data.decode('utf-8'))
    assert response_data['sentiment'] == 'POSITIVE'
    assert 0 <= response_data['confidence'] <= 1


def test_negative_sentiment(client):
    data = {
        'sentence': 'I hate you.'
    }
    response = client.post('/inference/sentiment_analysis', json=data)
    assert response.status_code == 200
    response_data = json.loads(response.data.decode('utf-8'))
    assert response_data['sentiment'] == 'NEGATIVE'
    assert 0 <= response_data['confidence'] <= 1
