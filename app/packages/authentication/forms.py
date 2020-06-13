from wtforms.fields import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    FileField,
    DateTimeField,
)
from wtforms.widgets import TextArea
from wtforms.validators import (
    Email,
    DataRequired,
    Length,
    ValidationError,
)
from flask_wtf import (
    FlaskForm,
    RecaptchaField,
)
from flask_login import current_user
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
    recaptcha = RecaptchaField()
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
    recaptcha = RecaptchaField()
    submit = SubmitField(
        label="Sign Up",
    )

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("[-] this email is already registered.")


class UpdateProfileForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.email.data = current_user.email
        self.name.data = current_user.name
        self.family.data = current_user.family
        self.username.data = current_user.username
        self.photo.data = current_user.photo
        self.role.data = current_user.role
        self.location.data = current_user.location
        self.about_me.data = current_user.about_me
        self.last_seen.data = current_user.last_seen

    email = StringField(
        label="email",
        validators=[Email(), Length(1, 64)],
    )
    password = PasswordField(
        label="password",
        validators=[Length(0, 64), ],
    )
    name = StringField(label="name", validators=[Length(0, 64), ])
    family = StringField(label="family", validators=[Length(0, 64), ])
    username = StringField(label="username", validators=[Length(0, 64), ])
    photo = FileField(label="profile picture")
    role = StringField(label="role")
    location = StringField(label="location")
    about_me = StringField(label="describe your self", widget=TextArea(), validators=[Length(0, 256), ])
    last_seen = DateTimeField(label="last seen")
    submit = SubmitField(
        label="Update",
    )
