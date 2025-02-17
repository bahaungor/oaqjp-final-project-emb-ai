"""
Emotion Detector Flask Application

Routes:
- `/`: Renders the index.html page.
- `/emotionDetector`: Analyzes text and returns detected emotions in JSON format.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
"""
Flask web application for detecting emotions in text input.
Uses the emotion_detector function from the EmotionDetection package.
"""

@app.route("/")
def render_index_page():
    """Renders the index.html page."""
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    """
    Detects the dominant emotion in the provided text.

    Returns:
        A JSON response containing the detected emotions or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return response

if __name__ == '__main__':
    app.run(debug=True, port=3000)
