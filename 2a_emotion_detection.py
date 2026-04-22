"""Emotion Detection using Watson NLP Library"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Run emotion detection on the given text using Watson NLP library.

    Returns a dictionary with scores for anger, disgust, fear, joy, and sadness,
    plus the dominant emotion. Returns None values if the input is blank (status 400).
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network'
        '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers, timeout=20)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_dict = json.loads(response.text)
    emotions = response_dict["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions["anger"],
        'disgust': emotions["disgust"],
        'fear': emotions["fear"],
        'joy': emotions["joy"],
        'sadness': emotions["sadness"],
        'dominant_emotion': dominant_emotion
    }