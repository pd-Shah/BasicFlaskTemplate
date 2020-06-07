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
)
from flask_wtf import FlaskForm


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
