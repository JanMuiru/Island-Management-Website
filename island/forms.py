from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, IntegerField
from wtforms.validators import DataRequired



class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email_address = EmailField(label='Email Address', validators=[DataRequired()])
    comment = StringField(label='Comment', validators=[DataRequired()])
    submit = SubmitField(label='Submit')



class ServicesForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email_address = EmailField(label='Email Address', validators=[DataRequired()])
    phone_number = IntegerField(label='Phone Number', validators=[DataRequired()])
    county = StringField(label='County', validators=[DataRequired()])
    town = StringField(label='Town', validators=[DataRequired()])
    enquiry = StringField(label='Enquire', validators=[DataRequired()])
    submit = SubmitField(label='Submit')
