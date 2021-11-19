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
    requirements1 = db.Column(db.String(500))
    requirements2 = db.Column(db.String(500))
    requirements3 = db.Column(db.String(500))
    
    

    def __init__(self, title, body, category, requirements1, requirements2, requirements3, location, user_id):
        self.title = title
        self.user_id = user_id
        self.body = body
        self.location = location
        self.category = category
        self.requirements1 = requirements1
        self.requirements2 = requirements2
        self.requirements3 = requirements3

    def __repr__(self):
        return '<Job {}>'.format(self.title)

class Application(db.Model):
    application_id = db.Column(db.Integer, primary_key=True)
    job_id =  db.Column(db.Integer, db.ForeignKey('job.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email_address = db.Column(db.String(50))
    location = db.Column(db.String(50))

    def __init__(self, first_name, last_name, location, about_me, answer1, answer2, answer3, job_id):
        self.first_name = first_name
        self.last_name = last_name
        self.job_id = job_id
        self.location = location
        self.about_me = about_me
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3


    def __repr__(self):
        return '<Application {}>'.format(self.last_name)




@login.user_loader
def load_user(id):
    return User.query.get(int(id))


