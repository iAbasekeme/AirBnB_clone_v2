#!/usr/bin/python3
"""A script that runs a flask application
"""
from flask import render_template
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
    return f'Python ' + text


@app.route('/number/<int:n>', strict_slashes=False)
def route_int(n):
    """A method that prints only an int
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n):
    """ A method that displays a html template
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
