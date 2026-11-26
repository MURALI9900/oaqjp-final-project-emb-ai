"""Emotion detection client for the Watson NLP Emotion Predict service."""

import requests

EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTION_KEYS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for input text."""
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            EMOTION_URL,
            json=payload,
            headers=headers,
            timeout=30,
        )
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }
        response.raise_for_status()
        predictions = response.json()["emotionPredictions"]
        scores = predictions[0]["emotion"]
        result = {emotion: scores[emotion] for emotion in EMOTION_KEYS}
        result["dominant_emotion"] = max(
            EMOTION_KEYS,
            key=lambda emotion: result[emotion],
        )
        return result
    except (requests.RequestException, KeyError, IndexError, TypeError, ValueError):
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
