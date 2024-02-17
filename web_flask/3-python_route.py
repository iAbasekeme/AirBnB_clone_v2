#!/usr/bin/python3
"""A script that runs a flask application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """A function that prints to stdout
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """A function that prints to stdout
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """A method that displays text
    """
    text = text.replace('_', ' ')
    return f'C ' + text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_kwargs(text='is cool'):
    """A method that displays text
    """
    text = text.replace('_', ' ')
    return f'C ' + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
