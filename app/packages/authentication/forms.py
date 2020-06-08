from wtforms.fields import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import (
    Email,
    DataRequired,
    Length,
    ValidationError,
)
from flask_wtf import FlaskForm
from .models import User


class LoginForm(FlaskForm):
    email = StringField(
        label="email",
        validators=[Email(), DataRequired(), Length(1, 64)],
    )
    password = PasswordField(
        label="password",
        validators=[DataRequired()]
    )
    remember_me = BooleanField(
        label="",
    )
    submit = SubmitField(
        label="login",
    )


class SignUpForm(FlaskForm):
    email = StringField(
        label="email",
        validators=[Email(), DataRequired(), Length(1, 64)],
    )
    password = PasswordField(
        label="password",
        validators=[DataRequired(), Length(1, 64), ],
    )
    submit = SubmitField(
        label="Sign Up",
    )

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("[-] this email is already registered.")
