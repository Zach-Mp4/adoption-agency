from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField(choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Pet Photo URL", validators=[Optional(),URL()])
    age = IntegerField("Pet Age", validators=[Optional(),NumberRange(min=0, max=30)])
    notes = StringField("Notes")
    available =  available = BooleanField("Available")

