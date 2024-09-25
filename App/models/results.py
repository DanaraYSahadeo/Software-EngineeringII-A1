from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

db = SQLAlchemy()

# class Results(db.Model):
#     results_id = db.Column(db.Integer, primary_key=True)
#     id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
#     competition_id = db.Column(db.Integer, ForeignKey('competitions.id'), nullable=False)
#     result = db.Column(db.String(120), nullable=False)
    
#     user = relationship('User', back_populates='results')
#     competition = relationship('Competition', back_populates='results')

#     def __init__(self, id, competition_id, result):
#         self.id = id
#         self.competition_id = competition_id
#         self.result = result

#     def get_json(self):
#         return {
#             'results_id': self.results_id,
#             'id': self.id,
#             'competition_id': self.competition_id,
#             'result': self.result
#         }

from App.database import db

class Results(db.Model):
    results_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), db.ForeignKey('user.username'), nullable=False)
    competition_name = db.Column(db.String(120), db.ForeignKey('competition.competition_name'), nullable=False)
    results = db.Column(db.String(120), nullable=False)

    user = db.relationship('User', back_populates='results')
    competition = db.relationship('Competition', back_populates='results')

    def __init__(self, username, competition_name, results):
        self.username = username
        self.competition_name = competition_name
        self.results = results

    def get_json(self):
        return {
            'results_id': self.results_id,
            'username': self.username,
            'competition_name': self.competition_name,
            'results': self.results,
        }
