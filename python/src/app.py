from flask import Flask, render_template, jsonify
from markovify import NewlineText
import requests as req
import os, sys

app = Flask(__name__)

# Set environmental values
if 'ENDPOINT' in os.environ and 'SUBSCRIPTION_KEY' in os.environ:
    endpoint = os.environ['ENDPOINT']
    subscription_key = os.environ['SUBSCRIPTION_KEY']

# 404 Not found
@app.errorhandler(404)
def invalid_uri(error):
    return jsonify({
        'error': {
            'code': 'Not found',
            'message': 'Page not found.'
        }
    }), 404

# Post url
@app.route('/', methods=['GET'])
def analyze_image():
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

    # Post image data
    image_path = './test.jpg'
    image_data = open(image_path, 'rb').read()

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)