from flask import Flask, request
import jsonify

application = Flask(__name__)
application.debug = True


@application.route("/")
def hello():
    return "Hello World"


# @application.route("/callback", methods={'GET'})
# def myFunc():
#     return


@application.route("/callback", methods=['POST'])
def callback():
    data = request.json
    print(data)
    if not(data['data']):
        return 'success'
    else:
        return 'love'

if __name__ == "__main__":
    application.run()