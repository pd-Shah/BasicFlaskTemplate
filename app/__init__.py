from os import makedirs
from os.path import join
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

    try:
        makedirs(
            name=app.instance_path,
            exist_ok=True,
        )
    except Exception as e:
        print(e)

    app.config.from_pyfile(filename="settings.py", silent=False)
    app.config["UPLOAD_DIR"] = join(app.config.get("BASE_DIR"), app.config.get("IMAGE_UPLOAD_FOLDER"))
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

    return app
