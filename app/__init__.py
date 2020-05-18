from os import makedirs
from flask import (
    Flask,
    render_template,
)
from settings import config


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

    app.config.from_pyfile(app.instance_path + "/settings.py")

    @app.route("/", methods=["GET", ])
    def test():
        return render_template("base.html")

    return app
