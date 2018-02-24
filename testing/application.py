from flask import Flask, request, Response
from flask_cors import CORS
import jsonify
import json
from sightengine.client import SightengineClient
import requests

application = Flask(__name__)
application.debug = True
CORS(application)


@application.route("/")
def hello():
    # return "Hello World"
    content = open('index.html').read()
    return Response(content, mimetype="text/html")


# @application.route("/callback", methods={'GET'})
# def myFunc():
#     return

# dynamic response
@application.route("/response/<id>", methods=['GET', 'POST'])
def lala(id):
    if request.method == 'GET':
        return 'ID: %s' % id
    else:
        thisData = json.dumps(request.json)
        print("hi" + thisData)
        return("received post" + thisData)

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
            url_id = data['media']['id']
            url = "http://watchsafehtv.us-east-1.elasticbeanstalk.com/response/" + url_id
            r = requests.post(url, data=data)
            return('yay')
        else:
            return('', 204)


if __name__ == "__main__":
    application.run()
