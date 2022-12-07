# This is a sample Python script.

import os
from flask import Flask, jsonify, make_response, request
from waitress import serve


app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if request.content_type in ["text/plain", "image/png", "image/jpeg"]:
            data = request.get_data()
            response = make_response(10*data)
            response.headers['Content-Type'] = request.content_type
            return response

        return jsonify(msg="bad data type"), 400
    except (KeyError, AttributeError) as e:
        print(e)
        return jsonify(msg="bad request"), 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5555))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('DEBUG', 'False').lower() in ('true', '1')

    if debug:
        app.run(host=host, debug=False, port=port)
    else:
        serve(app, host=host, port=port)
