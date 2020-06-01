from os import makedirs
from flask import (
    Flask,
    render_template,
)
from settings import config
from app.init import (
    db,
    migrate,
)
from app.packages.email.templates import WelcomeToYourSite
from app.packages.email import Email


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
    db.init_app(app=app)
    migrate.init_app(app, db, )

    @app.route("/", methods=["GET", ])
    def test():
        email = Email(WelcomeToYourSite)
        email.send("pd.shahsafi@gmail.com")
        return render_template("base.html")

    return app
