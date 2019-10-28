from flask import Flask, render_template, jsonify

from api import api

app = Flask(__name__)

app.register_blueprint(api)

@app.route('/')
def hello():
    return 'hello'

# 404 Not found
@app.errorhandler(404)
def invalid_uri(error):
    return jsonify({
        'error': {
            'code': 'Not found',
            'message': 'Page not found.'
        }
    }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)