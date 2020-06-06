from functools import wraps
from flask_login import current_user
from flask import abort
from app.init import login
from .models import User


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def check_to_login(user_obj, ):
    user = User.query.filter_by(email=user_obj.email.data).first()
    if user is None:
        return False
    if not user.verify_password(user_obj.password.data):
        return False
    return user


def permission_required(permission, ):
    def decorator(f, ):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)

            return f(*args, **kwargs)

        return wrapper

    return decorator
