from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    submit = SubmitField('Add Recipe')
    image = FileField("Recipe Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    meal_types = SelectMultipleField(
        'Meal Types',
        choices=[
            ('Breakfast', 'Breakfast'),
            ('Lunch', 'Lunch'),
            ('Dinner', 'Dinner'),
            ('Snack', 'Snack'),
            ('Dessert', 'Dessert'),
            ('Drink', 'Drink')
        ],
        coerce=str
    )
class ProfileForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=4, max=150)]
    )
    submit = SubmitField('Save Changes')        
