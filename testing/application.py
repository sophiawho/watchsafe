from flask import Flask, request, Response
from flask_cors import CORS
import jsonify

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
        return 'love'


if __name__ == "__main__":
    application.run()
