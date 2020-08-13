from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class projectsForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    pomodorosNumber = IntegerField('How many cycle for this Project?', validators=[DataRequired(message='A nubmer is required')])
    submit = SubmitField('Sumbit')