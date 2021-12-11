from flask_wtf import Form 
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class ContactForm(Form):
    name = TextField('Name of the Student', [validators.required('Please enter your name')])
    Gender = RadioField('Gender', choices= [('M','Male' ),('F', 'Female')])
    Address = TextAreaField("Address")

    email = TextField("Email", [validators.required("please enter your email address"),
                                  validators.Email("Please enter valid email address")])
    Age = IntegerField("Age")
    Language = SelectField('Languages Known', choices= [('cpp', 'C++'), ('py', 'Python')])


    submit = SubmitField("Submit") 