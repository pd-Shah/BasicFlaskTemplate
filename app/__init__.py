from os import makedirs
from flask_login import current_user
from flask import (
    Flask,
    render_template,
)
from settings import config
from app.init import (
    db,
    migrate,
    login,
    email,
)
from app.packages.email.templates import WelcomeToYourSite
from app.packages.email import Email
from app.packages import authentication
from app.packages import error


def create_app():
    app = Flask(
        import_name=__name__,
        instance_relative_config=True,
    )
    app.config.from_object(config)
    makedirs(
        name=app.instance_path,
        exist_ok=True,
    )
    app.config.from_pyfile(filename="settings.py", silent=False)
    db.init_app(app=app)
    migrate.init_app(app, db, )
    email.init_app(app, )
    login.init_app(app, )
    login.anonymous_user = authentication.models.AnonymousUser
    app.register_blueprint(authentication.bp)
    app.register_blueprint(error.bp)

    @app.route("/", methods=["GET", ])
    def index():
        return render_template("base.html")

    @app.shell_context_processor
    def load_data():
        u = authentication.models.User.query.get(1)
        return dict(
            app=app,
            User=authentication.models.User,
            Image=authentication.models.Image,
            Role=authentication.models.Role,
            u=u,
        )

    return app
