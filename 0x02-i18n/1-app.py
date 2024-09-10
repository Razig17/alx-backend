#!/usr/bin/env python3
"""Basic Babel app"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Config for Babel"""
    LANGUAGES = ['en', 'es']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
Babel = Babel(app)


@app.route('/')
def home() -> str:
    """Home page"""
    return render_template('1-index.html')
