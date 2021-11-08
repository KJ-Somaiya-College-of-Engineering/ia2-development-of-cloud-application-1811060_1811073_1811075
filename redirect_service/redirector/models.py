from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ResponseForm(FlaskForm):
    battery = StringField('battery')
    availableRam = StringField('availableRam')
    submit = SubmitField('submit')