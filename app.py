from flask import Flask, request, jsonify
from flask_cors import CORS
from handler.stream import Stream

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify('API 1.0')


@app.route('/checkStream', methods=['POST'])
def check_stream():
    check = False
    if 'key' in request.json.keys():
        stream = Stream()
        check = stream.check_on(request.json['key'])
    return jsonify({'check':check})

@app.route('/streamer/all', methods=['GET'])
def all_stremers():
    stream = Stream()
    return jsonify(stream.stremer_all()), 200



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)