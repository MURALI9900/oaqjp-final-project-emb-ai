"""Unit tests for the emotion detection application."""

import unittest
from unittest.mock import Mock, patch

import requests

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test valid responses and error handling."""

    @patch("emotion_detection.requests.post")
    def test_dominant_joy(self, mock_post):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.90,
                    "sadness": 0.04,
                }
            }]
        }
        mock_post.return_value = response
        result = emotion_detector("I love this new technology.")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(set(result), {
            "anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"
        })

    @patch("emotion_detection.requests.post")
    def test_dominant_anger(self, mock_post):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.90,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.01,
                    "sadness": 0.04,
                }
            }]
        }
        mock_post.return_value = response
        result = emotion_detector("I hate working long hours")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("emotion_detection.requests.post")
    def test_bad_request(self, mock_post):
        response = Mock()
        response.status_code = 400
        mock_post.return_value = response
        result = emotion_detector("invalid request")
        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])

    def test_blank_input(self):
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])

    @patch("emotion_detection.requests.post")
    def test_request_exception(self, mock_post):
        mock_post.side_effect = requests.RequestException("service unavailable")
        result = emotion_detector("some text")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
