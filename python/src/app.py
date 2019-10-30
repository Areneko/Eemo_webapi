from flask import Flask, render_template, jsonify
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
    # Subscription key
    subscription_key = '74c0278230bb4aa6aac723d66cc1cdd2'

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
    tagas = res.json()['description']['tags']

    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)