from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_us = TextAreaField('About us', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class JobForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Job Description', validators=[DataRequired()])
    requirements1 = StringField('List the Top 3 Requirements for This Role', validators=[DataRequired()])
    requirements2 = StringField('List the Top 3 Requirements for This Role', validators=[DataRequired()])
    requirements3 = StringField('List the Top 3 Requirements for This Role', validators=[DataRequired()])
    datecreated = StringField('Posted Date', validators=[DataRequired()])
    location = StringField('JobLocation', validators=[DataRequired()])
    submit = SubmitField()

class Application(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    location = StringField('Your Address', validators=[DataRequired()])
    about_me = StringField('About you: What experience, skill, and vision will you bring to this position? (within 500 characters)',validators=[Length(min=0, max=500)])
    req1_ans = StringField('Your Answer', validators=[DataRequired()])
    req2_ans = StringField('Your Answer', validators=[DataRequired()])
    req3_ans = StringField('Your Answer', validators=[DataRequired()])
    experience = Stringfield()


    submit = SubmitField()

