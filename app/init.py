from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.packages.email import Email

login = LoginManager()
login.login_view = "authentication.login"
db = SQLAlchemy()
migrate = Migrate()
email = Email()
