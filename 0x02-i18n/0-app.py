#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home()-> str:
    """Home page"""
    return render_template('0-index.html')
