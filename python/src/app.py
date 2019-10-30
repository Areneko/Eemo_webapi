from flask import Flask, jsonify, request
from markovify import NewlineText
import requests as req
import os, sys

app = Flask(__name__)

# Set environmental values
if 'ENDPOINT' in os.environ and 'SUBSCRIPTION_KEY' in os.environ:
    endpoint = os.environ['ENDPOINT']
    subscription_key = os.environ['SUBSCRIPTION_KEY']

# Post url
@app.route('/', methods=['POST'])
def analyze_image():
    # Get image data from body
    try:
        json = request.json()
        image_data = json['image_data']
    except Exception as e:
        return error_handler(e)

    # Post header
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key
    }

    # Post params
    params = {
        'visualFeatures': 'Description',
        'language': 'ja'
    }

    # Call API and get tags
    res = req.post(endpoint, headers=headers, params=params, data=image_data)
    tags = res.json()['description']['tags']

    splited_text = open('./resources/splited.txt').read()
    text_model = NewlineText(splited_text)

    for tag in tags:
        try:
            sentence = text_model.make_sentence_with_start(tag, tries=300, max_overlap_ratio=0.9).replace(' ', '')
            return sentence
        except:
            pass

# Error handling
@app.errorhandler(Exception)
def error_handler(e):
    return jsonify({
        'error': {
            'type': e.name,
            'message': e.description
        }
    }), e.code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)