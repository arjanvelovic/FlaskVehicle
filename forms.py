from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    # email, password, submit
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class UserSignupForm(FlaskForm):
    # email, password, submit
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    phone_number = StringField('Phone Number', validators = [DataRequired()])
    address = StringField('Address', validators = [DataRequired()])
    submit_button = SubmitField()

class ProfileButton(FlaskForm):
    submit_button = SubmitField()

class EditProfile(FlaskForm):
    # email, password, submit
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    phone_number = StringField('Phone Number', validators = [DataRequired()])
    address = StringField('Address', validators = [DataRequired()])
    submit_button = SubmitField()

class VehiclesForm(FlaskForm):
    submitModel3 = SubmitField(label="Build Your Model 3 Here", name= "Model3", id="Model3")
    submitModelS = SubmitField(label="Build Your Model S Here", name= "ModelS", id="ModelS")
    submitModelX = SubmitField(label="Build Your Model X Here", name= "ModelX", id="ModelX")
    submitModelY = SubmitField(label="Build Your Model Y Here", name= "ModelY", id="ModelY")

class ColorTrimForm(FlaskForm):
    # email, password, submit
    color = RadioField('Color', choices=['white', 'black', 'red'])
    trim = RadioField('Trim', choices=['1.0', '2.0', '3.0'])
    submit_button = SubmitField()