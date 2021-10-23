from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

##WTForm
class CreateUrlForm(FlaskForm):
    product_url = StringField("Insert URL Here", validators=[DataRequired(), URL()])
    submit = SubmitField("Submit URL")

