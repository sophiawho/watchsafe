from flask import Flask, jsonify, render_template, request
import requests
import string
import os
import json

app = Flask(__name__)

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('test.html', name=name)

@app.route("/")
def index():
    return render_template('index.html')

# @app.route("/callback/", methods=['POST'])
# def callback():
# 	data = request.json
# 	# return data
# 	# return render_template('test.html', data=data)
# 	return jsonify(data=data)

if __name__ == "__main__":
	app.run(port=8080, debug=True)