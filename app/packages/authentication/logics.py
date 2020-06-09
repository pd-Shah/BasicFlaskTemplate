from os.path import join
from functools import wraps
from flask_login import current_user
from flask import (
    abort,
    current_app,
)
from app.init import (
    login,
    db,
)
from .models import (
    User,
    Image,
)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def check_to_login(user_obj, ):
    user = User.query.filter_by(email=user_obj.email.data).first()
    if user is None:
        return False
    if not user.verify_password(user_obj.password.data):
        return False
    user.update_last_seen()
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


def get_user_by_username(username):
    user = User.query.filter_by(username=username).first_or_404()
    return user


def check_to_sign_up(user_obj, ):
    password = user_obj.password.data
    email = user_obj.email.data
    user = User(email=email)
    user.password = password
    db.session.add(user)
    db.session.commit()


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config.get("ALLOWED_EXTENSIONS")


def get_last_image_id():
    last_record_id = 1
    i = Image.query.order_by(Image.id.desc()).first()
    if i is not None:
        last_record_id = i.id + 1
    return str(last_record_id)


def save_file(file):
    extension = file.filename.rsplit(".", 1)[1].lower()
    filename = get_last_image_id() + '.' + extension
    file.save(join(current_app.config['UPLOAD_DIR'], filename))
    photo = Image()
    photo.extension = extension
    db.session.add(photo)
    current_user.photos.append(photo)
    db.session.commit()
    return filename
