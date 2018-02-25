from flask import Flask, request, Response
from flask_cors import CORS
import jsonify
import json
from sightengine.client import SightengineClient
import requests
# from flask.ext.socketio import SocketIO, emit
from flask_socketio import SocketIO, emit

application = Flask(__name__)
application.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(application)
application.debug = True
CORS(application)


@application.route("/")
def hello():
    # return "Hello World"
    content = open('index.html').read()
    return Response(content, mimetype="text/html")

@application.route("/test")
def uh():
    socketio.emit('my response', {'data': 'got it!'}, namespace='/test')
    return "yes"

# dynamic response
@application.route("/response/<id>")
def lala(id):
    content = open('analytics.html').read()
    return Response(content, mimetype="text/html")

@application.route("/test", methods=['POST'])
def whee():
    return "success"

@application.route("/callback", methods=['POST'])
def callback():
    data = request.json
    print(data)
    if not (data['data']):
        return 'success'
    else:
        if (data['data']['status'] == 'finished'):
            socketio.emit('my response', data, namespace='/'+data['media']['id'])
            print('done')
            return('', 200)
        else:
            socketio.emit('my response', data, namespace='/'+data['media']['id'])
            return('', 204)


if __name__ == "__main__":
    socketio.run(application)
