#!/usr/bin/python3
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close_session():
    """"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_html():
    from models.state import State
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
