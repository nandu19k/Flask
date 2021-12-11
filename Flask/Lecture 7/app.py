from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'nerchuko'

class ContactForm(Form):
    name = StringField('What is your name?')
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():

    contact = ContactForm()
    name = False

    if contact.validate_on_submit():
        name = contact.name.data
        contact.name.data = ' '
    return render_template('index.html', contact = contact, name=name)


if __name__ == '__main__':
    app.run(debug=True)


