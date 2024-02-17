#!/usr/bin/python3
"""Docs
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Docs
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Docs
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """Docs
    """
    text = text.replace('_', ' ')
    return f'C '+ text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
