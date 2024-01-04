from .extensions import db
import string
from random import choices
from datetime import datetime

class ShortenedURL(db.Model):
    """
    Model for storing information about shortened URLs.
    """
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512), nullable=False)
    short_code = db.Column(db.String(6), unique=True, nullable=False)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.short_code:
            self.short_code = self.generate_short_code()

    def generate_short_code(self):
        """
        Generates a unique short code for the URL.
        """
        characters = string.ascii_letters + string.digits
        short_code = ''.join(choices(characters, k=6))

        if self.__class__.query.filter_by(short_code=short_code).first():
            return self.generate_short_code()

        return short_code
