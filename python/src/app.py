from flask import Flask, render_template, jsonify

app = Flask(__name__)

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
    return 'test'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)