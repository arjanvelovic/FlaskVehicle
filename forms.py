from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, Length

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField(label='Sign In')

class UserSignupForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(8)])
    phone_number = StringField('Phone Number', validators = [DataRequired(), Length(10,12)])
    address = StringField('Address', validators = [DataRequired()])
    submit_button = SubmitField(label='Create an Account')

class ProfileButton(FlaskForm):
    submit_button = SubmitField(label="Edit Profile Details")

class EditProfile(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    phone_number = StringField('Phone Number')
    address = StringField('Address')
    submit_button = SubmitField(label = "Save Changes")

class VehiclesForm(FlaskForm):
    submitModel3 = SubmitField(label="Build Your Model 3 Here", name= "Model3", id="Model3")
    submitModelS = SubmitField(label="Build Your Model S Here", name= "ModelS", id="ModelS")
    submitModelX = SubmitField(label="Build Your Model X Here", name= "ModelX", id="ModelX")
    submitModelY = SubmitField(label="Build Your Model Y Here", name= "ModelY", id="ModelY")

class ColorTrimForm(FlaskForm):
    color = RadioField('Color', choices=[('white', 'Pearl White'),('black', 'Solid Black'), ('red', 'Race Red'), ('silver', 'Midnight Silver')])
    trim = RadioField('Color', choices=[('trim1', 'Basic'),('trim2', 'Long Range'), ('trim3', 'Performance')])
    submit_button = SubmitField(label="Add to Cart")