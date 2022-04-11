from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class TarotPostForm(FlaskForm):
    title = StringField('Recipient/Recipients', validators=[DataRequired()])
    spread = StringField('Spread', validators=[DataRequired()])
    card1 = StringField('First Card', validators=[DataRequired()])
    card2 = StringField('Second Card', validators=[DataRequired()])
    card3 = StringField('Third Card', validators=[DataRequired()])
    reflection = TextAreaField('Reflection', validators=[DataRequired()])
    submit = SubmitField('Post')