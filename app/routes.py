from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import ApplicationForm, LoginForm, RegistrationForm, EditProfileForm, JobForm
from app.models import Application, User, Job
from datetime import datetime


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@login_required
def index():

    jobs= Job.query.all()
    return render_template("index.html", title='Home Page', user = user, jobs=jobs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    jobs= Job.query.all()
    return render_template('user.html', user=user, jobs=jobs, )

@app.route('/my_jobs')
@login_required
def my_jobs():
    jobs = current_user.jobs
    return render_template('my_jobs.html', jobs=jobs)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_us = form.about_us.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_us.data = current_user.about_us
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

@app.route('/createjob', methods=['GET', 'POST'])
def createpost():
    form = JobForm()
    if form.validate_on_submit():
        print('Posted')
        title = form.title.data
        body = form.body.data
        category=form.category.data
        location = form.location.data
        requirements1= form.requirements1.data
        requirements2 = form.requirements2.data
        requirements3= form.requirements3.data
        new_post = Job(title, body, location=location, category=category, user_id=5, requirements1=requirements1, requirements2=requirements2, requirements3=requirements3)
        db.session.add(new_post)
        db.session.commit()
    return render_template('createjob.html', form=form)


@app.route('/application/')
@login_required
def apply():
    form = ApplicationForm()
    if form.validate_on_submit():
        print('Applied')
        first_name = form.first_name.data
        last_name = form.last_name.data        
        location = form.location.data
        about_me = form.about_me.data
        tagline =form.tagline.data
        location = form.location.data
        answer1= form.answer1.data
        answer2 = form.answer2.data
        answer3= form.answer3.data
        # job_id= int(Job.id)
        new_application = Application(first_name, last_name, tagline, location, about_me, user_id=5, answer1=answer1, answer2=answer2, answer3=answer3)
        db.session.add(new_application)
        db.session.commit()
    return render_template('application.html', form=form)


@app.route('/my_jobs/<int:job_id>')
def job_detail(job_id):
    job = Job.query.get(job_id)
    application = Application.query.filter_by(job_id = job_id)

    return render_template('job_apps.html', job=job, application=application)



@app.route('/my_jobs/<int:job_id>/update', methods=['GET', 'POST'])
@login_required
def job_update(job_id):
    job = Job.query.get_or_404(job_id)
    if job.author.id != current_user.id:
        flash('That is not your job. You may only edit jobs you have created.', 'danger')
        return redirect(url_for('app.job_detail'))
    form = JobForm()
    if form.validate_on_submit():
        new_title = form.title.data
        new_content = form.content.data
        print(new_title, new_content)
        job.title = new_title
        job.content = new_content
        db.session.commit()

        flash(f'{job.title} has been saved', 'success')
        return redirect(url_for('app.job_detail', job_id=job.id))

    return render_template('job_update.html', job=job, form=form)


@app.route('/my_jobs/<int:job_id>/delete', methods=['POST'])
@login_required
def job_delete(job_id):
    job = Job.query.get_or_404(job_id)
    if job.author != current_user:
        flash('You can only delete your own jobs', 'danger')
        return redirect(url_for('app.my_jobs'))

    db.session.delete(job)
    db.session.commit()

    flash(f'{job.title} has been deleted', 'success')
    return redirect(url_for('app.my_jobs', job_id=Job.id))
