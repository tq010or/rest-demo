#!/usr/bin/env python
"""
This is a demo for finding location indicative words relative to a user's input, i.e., city name
"""

from flask import Flask, render_template, request
try:
    import ujson as json
except ImportError:
    import json


# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=["POST"])
def rest_post_demo():
    req_data = request.form["data"] 
    print req_data, type(req_data)
    resp_data = json.dumps({"resp_json_data": req_data + " is processed by POST REST API!"})
    print resp_data, type(resp_data)
    return resp_data


@app.route('/get')
def rest_get_demo():
    req_data = request.args.get("data")
    print req_data, type(req_data)
    resp_data = json.dumps({"resp_json_data": req_data + " is processed by GET REST API!"})
    print resp_data, type(resp_data)
    return resp_data

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("5000"),
        debug=True
    )

