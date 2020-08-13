from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,BooleanField,SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class projectsForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    pomodorosNumber = IntegerField('How many cycle for this Project?', validators=[DataRequired(message='A nubmer is required')])
    submit = SubmitField('Sumbit')

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