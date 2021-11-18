from hashlib import md5
from app import login
from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    jobs = db.relationship('Job', backref='author', lazy='dynamic')
    # employer = db.Column(db.String(120), index=True, unique=True)
    about_us = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
        digest, size)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.String(140))
    category= db.Column(db.String(100))
    datecreated = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    location = db.Column(db.String(100))
    
    

    def __init__(self, title, body, location, user_id):
        self.title = title
        self.user_id = user_id
        self.body = body
        self.location = location


    def __repr__(self):
        return '<Job {}>'.format(self.body)

class Application(db.Model):
    application_id = db.Column(db.Integer, primary_key=True)
    job_id =  db.Column(db.Integer, db.ForeignKey('job.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email_address = db.Column(db.String(50))
    city_location = db.Column(db.String(50))




@login.user_loader
def load_user(id):
    return User.query.get(int(id))


