#!/usr/bin/python3
"""A script that runs a flask application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_world():
    """ A method that print to stdout
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
