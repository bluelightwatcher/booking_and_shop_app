from flask import Flask
from flask_restx import Api
from app.config import config
from app.extensions import db, init_db  # Import db & helper function
from app.routes import registerblueprint

def create_app(config_name='development'):
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)

    # Apply configuration
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)

    # Initialize the database properly
    init_db(app)

    # Register Blueprints for modular routes
    registerblueprint(app)

    # Initialize API
    api = Api(app, version="1.0", title="Clou API", 
              description="Clou doré Application API", doc="/lecloudore/api")

    return app
