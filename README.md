# Final project

## Emotion Detector

This repository contains the IBM Applied AI final project: an emotion detection web application built with Python, the Watson NLP Emotion Predict API, and Flask.

### Features
- Detects anger, disgust, fear, joy, and sadness.
- Returns the five emotion scores and the dominant emotion.
- Handles invalid or blank input.
- Includes unit tests and a Flask web interface.

### Run locally
1. Install dependencies: `python3 -m pip install -r requirements.txt`
2. Start the application: `python3 server.py`
3. Open `http://127.0.0.1:5000` in your browser.

The Watson NLP service must be reachable for live emotion predictions.
