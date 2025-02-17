import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

# Configuration variables (replace these with your actual values)
username = 'dev_work'
password = 'Mamachin3!'
hostname = 'localhost'
database_name = 'clou'

# Create the SQLAlchemy URI for database connection
SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}'

# Create an engine to check/create the database
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{hostname}/', pool_recycle=3600)

def create_database_if_not_exists():
    """Create the database if it doesn't exist."""
    try:
        with engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))
            print(f"Database '{database_name}' created or already exists.")
    except OperationalError as e:
        print(f"Error creating database: {e}")

create_database_if_not_exists()


class Config:
    """Base configuration class."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI  # Use MySQL database


class DevelopmentConfig(Config):
    """Configuration for development environment."""
    DEBUG = True


class ProductionConfig(Config):
    """Configuration for production environment."""
    DEBUG = False


# Dictionary for environment-based configurations
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

