#!/usr/bin/python3
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close_session():
    """Teardown method to manage app context"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_html():
    """Displat a html page with the states list"""
    from models.state import State
    states = storage.all(State).values()
    ordered_states = sorted(states, key=lambda x: x.name)
    return render_template("7-states_list.html", ordered_states=ordered_states)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
