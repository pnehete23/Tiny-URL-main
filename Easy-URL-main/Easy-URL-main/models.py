from .extensions import database
from datetime import datetime

class URL_shortner(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), nullable=False)
    content = database.Column(database.Text, nullable=False)
    created_at = database.Column(database.DateTime, default=datetime.utcnow)
    updated_at = database.Column(database.DateTime, onupdate=datetime.utcnow)

    def __init__(self, title, content):
        self.title = title
        self.content = content
