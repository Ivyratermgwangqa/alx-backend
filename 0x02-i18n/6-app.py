#!/usr/bin/env python3
"""
Flask app with Babel setup, locale selection, and user preferred locale.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

class Config:
    """
    Configuration class for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """
    Retrieve the user from the mock database.
    Returns:
        The user dictionary or None.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None

@babel.localeselector
def get_locale():
    """
    Select the best match language from the request, URL parameter, or user settings.
    Returns:
        The best match language.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    user = getattr(g, 'user', None)
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.before_request
def before_request():
    """
    Function to run before each request.
    Sets the global user based on the login_as parameter.
    """
    g.user = get_user()

@app.route('/')
def index():
    """
    Route for the index page.
    Returns:
        Rendered HTML template for the index page.
    """
    return render_template('6-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
