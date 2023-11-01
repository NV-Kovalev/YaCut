from datetime import datetime

from . import db
from settings import BASE_URL


class URLMap(db.Model):
    """
    Модель URL для редиректа.
    """

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            short_link=f'{BASE_URL}{self.short}',
            url=self.original
        )

    def from_dict(self, data):
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])
