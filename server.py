"""Flask web application for the emotion detector."""

from flask import Flask, jsonify, render_template, request

from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Render the emotion detector page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze text submitted by the browser."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text, 200


@app.errorhandler(400)
def bad_request(error):
    """Return a consistent message for bad requests."""
    del error
    return jsonify({"error": "Invalid text! Please try again!"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
