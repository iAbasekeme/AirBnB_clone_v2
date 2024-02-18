#!/usr/bin/python3
"""A script that runs a flask application
"""
from flask import render_template
from flask import Flask
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """Teardown method to close storage after app context is destroyed
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def index():
    """Route to display a HTML page with a list of states
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
