''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    output = (
        "For the given statement, the system response is "
        f"anger: {response['anger']}, "
        f"disgust: {response['disgust']}, "
        f"fear: {response['fear']}, "
        f"joy: {response['joy']} and "
        f"sadness: {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    
    return output

    ## Extract the label and score from the response
    #label = response['label']
    #score = response['score']

    ## Check if the label is None, indicating an error or invalid input
    #if label is None:
    #    return "Invalid input! Try again."
    #else:
    #    # Return a formatted string with the sentiment label and score
    #    return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    """" This functions executes the flask app and deploys it on localhost:5000 """
    app.run(host="0.0.0.0", port=5000)
    
