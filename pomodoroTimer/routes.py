from flask import render_template, url_for, flash, redirect, request, jsonify,session
from pomodoroTimer import app,db,bcrypt
from pomodoroTimer.forms import projectsForm,RegistrationForm, LoginForm,SelectProjectsForm
from pomodoroTimer.models import User,Project
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/history')
@login_required
def history():
    projects = Project.query.filter_by(user_id=current_user.id).all()
    return render_template('history.html',projects=projects)    

@app.route('/saveProjectToHistory', methods =["POST"])
@login_required
def saveProjectToHistory():
    cyclesDone = request.get_json(force = True)
    project = Project.query.filter_by(user_id=current_user.id).filter_by(title=session["project"]).first()
    previousDoneCycles = project.cyclesDone

    # sum new cycles with  cycles in the database
    allCyclesDone = int(cyclesDone)+int(previousDoneCycles)

    #update database
    project.cyclesDone = allCyclesDone
    db.session.commit()
    return "saved"

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',page_name='Home')

@app.route('/timer', methods=['GET', 'POST'])
@login_required
def timer():
    return render_template('timer.html', page_name="Pomodoro Timer",project=session.get('project'))


@app.route("/addProject", methods=['GET', 'POST'])
@login_required
def addProject():
    projectsform = projectsForm()
    if projectsform.validate_on_submit():
        projectName = projectsform.name.data
        project = Project(title=projectName,user_id=current_user.id)
        db.session.add(project)
        db.session.commit()
        flash(f'project {projectName} Added','success')
        return(redirect(url_for('selectProject')))
    return render_template('addProject.html', page_name="Add a Project",projectsform=projectsform)

@app.route('/selectProject', methods=['GET', 'POST'])
@login_required
def selectProject():
    user = User.query.get(current_user.id)
    myProjects= user.projects

    form = SelectProjectsForm()
    form.name.choices= myProjects
    if request.method == 'POST':
        session['project'] = form.name.data 
        return(redirect(url_for('timer')))
    return render_template('selectProject.html', page_name="Select a Project to work on", form=form)

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
    session.clear()
    flash(f'You have been logged out','success')
    return redirect(url_for('home'))