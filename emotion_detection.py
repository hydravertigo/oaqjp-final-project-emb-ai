import requests
import json

def emotion_detector(text_to_analyse):

    # Define the URL for the emotion prediction API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_output = json.loads(response.text)

    # create empty dictionary that will hold our values
    response_dict = {}

    # Get the emotion attribute scores
    response_dict['anger'] = formatted_output['emotionPredictions'][0]['emotion']['anger']
    response_dict['disgust'] = formatted_output['emotionPredictions'][0]['emotion']['disgust']
    response_dict['fear'] = formatted_output['emotionPredictions'][0]['emotion']['fear']
    response_dict['joy'] = formatted_output['emotionPredictions'][0]['emotion']['joy']
    response_dict['sadness'] = formatted_output['emotionPredictions'][0]['emotion']['sadness']

    # figure out which sentiment has the greatest value
    response_dict['dominant_emotion'] = max(response_dict, key=response_dict.get)

    # Returnt he dictionary
    return response_dict


    
