from flask import render_template,flash
from pomodoroTimer import app
from pomodoroTimer.forms import projectsForm
#from pomodoroTimer.models import 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/timer', methods=['GET', 'POST'])
def timer():
    form = projectsForm()
    if form.validate_on_submit():
        flash(f'project {form.name.data} Added','success')
    return render_template('timer.html',form = form)
    
@app.route('/projects', methods=['GET', 'POST'])
def projects():
    form = projectsForm()
    if form.validate_on_submit():
        return 'Form successfully submitted'
    return render_template('projects.html',form = form)