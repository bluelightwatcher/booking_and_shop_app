from app.extensions import db
from flask_sqlalchemy.model import Model
from sqlalchemy import Column, String, DateTime
import uuid
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        """Save or update the object in the database"""
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def delete(self):
        """Delete the object from the database"""
        db.session.delete(self)
        db.session.commit()
