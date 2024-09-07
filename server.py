"""
Emotion Detector Flask application.
This module handles requests for emotion detection using text input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_receiver():
    """
    Receives text from the request and returns the emotion analysis.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    res_string = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )

    return res_string

@app.route("/")
def render_web_page():
    """
    Renders the main web page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
