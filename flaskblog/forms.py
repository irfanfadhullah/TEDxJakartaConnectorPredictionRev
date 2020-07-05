from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp

class PredictForm (FlaskForm):
    
    
    submit_test = SubmitField ('Submit')

    