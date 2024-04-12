#!/usr/bin/python3
"""Script to starts the Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def welcome():
    """Display a welcome message for main route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Display 'HBNB' for the hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Display 'C ' followed by the text value"""
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def p_text(text="is cool"):
    """Display 'Python ' followed by the text value"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
        """Displays 'n is a number' only if it is"""
        return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
