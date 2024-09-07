import requests
import json

def emotion_detector(text_to_analyse): 
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url=URL, json=obj, headers=Headers)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_res = json.loads(response.text)

    anger_score = formatted_res['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_res['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_res['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_res['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_res['emotionPredictions'][0]['emotion']['sadness']
    dominant_emotion = ''

    highest_val = 0
    for key in formatted_res['emotionPredictions'][0]['emotion']:
        value = formatted_res['emotionPredictions'][0]['emotion'][key]

        if value > highest_val:
            highest_val = value
            dominant_emotion = key

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }