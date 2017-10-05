from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, SubmitField, StringField, PasswordField, validators
from wtforms.validators import InputRequired, DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    n_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    accept_tos = BooleanField('Remember Me', [validators.DataRequired()])
    submit = SubmitField("Login")


    def validate_username(self, field):
        if field.data != USERNAME:
            raise ValidationError("Invalid username")

    def validate_password(self, field):
        if field.data != PASSWORD:
            raise ValidationError("Invalid password")

class RegistrationForm(Form):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=2, max=40)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=2, max=40)])
    n_name = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=25),
                                          EqualTo('confirm', message='Passwords must match')
                                          ])
    email = StringField('Email Address', validators=[DataRequired(), Email(message=None),
                                                     Length(min=6, max=35)
                                                     ])
    age = StringField('Age', validators=[DataRequired(), Length(min=1, max=3)])
    confirm = PasswordField('Repeat Password')


    def validate(self):
        initial_validation = super(RegistrationForm, self).validate()
        if not initial_validation:
            return False
        user = my_app.models.Users.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True
