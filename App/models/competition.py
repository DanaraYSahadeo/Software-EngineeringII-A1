from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

from App.database import db

class Competition(db.Model):
    competition_id = db.Column(db.Integer, primary_key=True)
    competition_name = db.Column(db.String(120), nullable=False)

    results = db.relationship('Results', back_populates='competition')

    def __init__(self, competition_name):
        self.competition_name = competition_name

    def get_json(self):
        return {
            'competition_id': self.competition_id,
            'competition_name': self.competition_name,
        }
