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
