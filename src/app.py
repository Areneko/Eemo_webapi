from flask import Flask, jsonify, request
from markovify import NewlineText
import requests as req
import os, sys, base64

app = Flask(__name__)

# Set environmental values
from dotenv import load_dotenv
from os.path import join, dirname

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

if 'ENDPOINT' in os.environ and 'SUBSCRIPTION_KEY' in os.environ:
    endpoint = os.environ.get('ENDPOINT')
    subscription_key = os.environ.get('SUBSCRIPTION_KEY')

# Test url
@app.route('/', methods=['GET'])
def test():
    return 'BIND OK'

# Post url
@app.route('/api/generate', methods=['POST'])
def analyze_image():
    # Get image data from body
    file = request.files['file']

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
    try:
        res = req.post(endpoint, headers=headers, params=params, data=file)
    except Exception(e):
        print(e)
    print(res.json())
    tags = res.json()['description']['tags']

    splited_text = open('./resources/splited.txt').read()
    text_model = NewlineText(splited_text)

    for tag in tags:
        try:
            sentence = text_model.make_sentence_with_start(tag, tries=300, max_overlap_ratio=0.7).replace(' ', '')
            return sentence
        except:
            pass
    return 'Could not create sentence'

# Error handling
@app.errorhandler(Exception)
def error_handler(e):
    return jsonify({
        'error': True,
        'message': 'Some error occured in server.'
    }), 500

port = os.environ.get('PORT')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)