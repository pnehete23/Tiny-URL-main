from flask import Flask
from .extensions import db  # Importing the SQLAlchemy instance
from .routes import url_shortener

def initialize_url_shortener(config='config.py'):
    """
    Initialize the Flask application for URL shortening.

    Args:
    - config: Configuration file for the application.

    Returns:
    - Flask application instance.
    """
    flask_app = Flask(__name__)

    # Load configurations from the specified file.
    flask_app.config.from_pyfile(config)

    # Initialize the database with the Flask app.
    db.init_app(flask_app)

    # Register the URL shortening routes.
    flask_app.register_blueprint(url_shortener)
    
    return flask_app


