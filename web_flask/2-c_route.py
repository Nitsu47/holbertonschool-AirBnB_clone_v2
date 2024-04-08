#!/usr/bin/python3
"""
script that starts flask web application
"""
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def HBNB():
    """
    return Hello HBNB
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    return hbnb
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """
    return C followed by the value of the text variable
    """
    return "C " + text.replace("_", " ")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")