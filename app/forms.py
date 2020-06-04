from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class RegForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	surname = StringField('Surname', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	password_hash = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Sign up')

class ReqLeave(FlaskForm):
	d = IntegerField('Enter num of days', validators=[DataRequired()])
	submit = SubmitField('Ok')