from app.extensions import db
from app.model.base_model import BaseModel
from sqlalchemy import Column, String, Boolean
import re

class User(BaseModel):
    __tablename__ = "users"  

    # Define the columns for the user model
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    """
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()  
        self.first_name = self.first_name_check(first_name)
        self.last_name = self.last_name_check(last_name)
        self.is_admin = is_admin
        self.email = self.email_check(email)
        self.password_hash = password  
    """
    @staticmethod
    def first_name_check(first_name):
        """Ensure first name is a string and not too long"""
        if len(first_name) > 50:
            raise ValueError("Name is too long")
        elif not isinstance(first_name, str):
            raise TypeError("Name must be a string")
        return first_name

    @staticmethod
    def last_name_check(last_name):
        """Ensure last name is a string and not too long"""
        if len(last_name) > 50:
            raise ValueError("Name is too long")
        elif not isinstance(last_name, str):
            raise TypeError("Name must be a string")
        return last_name

    @staticmethod
    def email_check(email):
        """Check that the email is in a valid format"""
        regex = r'^[a-zA-Z0-9.+-]+@[a-zA-Z]+\.[a-zA-Z0-9]{2,}+$'
        if not re.match(regex, email):
            raise ValueError("Invalid email format")
        return email
