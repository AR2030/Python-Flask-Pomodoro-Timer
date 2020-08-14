from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,BooleanField,SubmitField,PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from pomodoroTimer.models import User

class projectsForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    pomodorosNumber = IntegerField('How many minutes do you need for this Project?', validators=[DataRequired(message='A nubmer is required')])
    submit = SubmitField('Sumbit')

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')