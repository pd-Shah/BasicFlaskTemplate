from faker import Faker
from app.init import db
from app import create_app
from app.packages.authentication.models import User, Role

app = create_app()

with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()
    db.session.commit()
    fake = Faker()

    admin = Role(name="admin")
    moderator = Role(name="moderator")
    user_role = Role(name="user")
    db.session.add_all([admin, moderator, user_role])
    db.session.commit()

    admin = User(name="pd", username="admin", email="pd.shahsafi@gmail.com")
    moderator = User(name="moderator", username="moderator", email="moderator@gmail.com")

    user = User(name=fake.name(), username=fake.name(), email=fake.email(), role=user_role)
    db.session.add(user)
    db.session.commit()

    user = User(name=fake.name(), username=fake.name(), email=fake.email(), role=user_role)
    db.session.add(user)
    db.session.commit()

    user = User(name=fake.name(), username=fake.name(), email=fake.email(), role=user_role)
    db.session.add(user)
    db.session.commit()