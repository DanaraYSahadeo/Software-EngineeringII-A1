from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # Either 'admin' or 'student'

    results = db.relationship('Results', back_populates='user')

    def __init__(self, username, password, role='student'):
        self.username = username
        self.set_password(password)
        self.role = role  # Default role is 'student'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username,
        }

    def is_admin(self):
        return self.role == 'admin'

    def is_student(self):
        return self.role == 'student'

