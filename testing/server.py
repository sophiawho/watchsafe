from flask import Flask, request, redirect
import jsonify

application = Flask(__name__)
application.debug = True


@application.route("/")
def hello():
    return "Hello World"


# @application.route("/callback", methods={'GET'})
# def myFunc():
#     return

@application.route("/leRedirect")
def hi():
    return "You were redirected"

@application.route("/callback", methods=['POST'])
def callback():
    # data = request.json
    # print(data)
    # if not(data['data']):
    #     return 'success'
    # else:
    #     return 'love'
    return redirect('/leRedirect')
if __name__ == "__main__":
    application.run()