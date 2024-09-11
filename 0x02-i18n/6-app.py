#!/usr/bin/env python3
"""Basic Babel app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """Return a user dictionary or None if the ID cannot be found"""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id), None)


@app.before_request
def before_request() -> None:
    """find a user if any, and set it as a global on flask.g.user"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Get best matching language"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user["locale"] in app.config['LANGUAGES']:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """Home page"""
    return render_template('5-index.html', user=g.user)
