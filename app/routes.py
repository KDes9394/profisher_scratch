from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kento'}
    jobs = [
        {
            'author': {'username': 'Jake'},
            'job_desc': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Terry'},
            'job_desc': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, jobs=jobs)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)