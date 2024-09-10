#!/usr/bin/env python3
"""Basic Babel app"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
from typing import Union


class Config:
    """Config for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Get best matching language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """Home page"""
    return render_template('2-index.html', home_title=_("home_title"),
                           home_header=_("home_header"))
