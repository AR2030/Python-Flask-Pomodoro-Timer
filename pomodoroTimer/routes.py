from flask import render_template, url_for, flash, redirect, request
from pomodoroTimer import app,db,bcrypt
from pomodoroTimer.forms import projectsForm,RegistrationForm, LoginForm,SelectProjectsForm
from pomodoroTimer.models import User,Project
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',page_name='Home')

@app.route('/timer', methods=['GET', 'POST'])
@login_required
def timer():
    projectsform = projectsForm()
    if projectsform.validate_on_submit():
        projectName = projectsform.name.data
        project = Project(title=projectName,user_id=current_user.id)
        db.session.add(project)
        db.session.commit()
        flash(f'project {projectName} Added','success')
    return render_template('timer.html', page_name="Timer" ,projectsform = projectsform,SelectProjectsForm=SelectProjectsForm())

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', page_name='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'Wellcome {current_user.username}','success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', page_name='Login', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash(f'You have been logged out','success')
    return redirect(url_for('home'))