"""Import and initialize the db here"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """Initialize the database and create tables if needed."""
    with app.app_context():
        db.create_all()
