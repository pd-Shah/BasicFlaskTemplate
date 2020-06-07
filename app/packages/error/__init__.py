from flask import (
    Blueprint,
    render_template,
)

bp = Blueprint(
    "error",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/error"
)


@bp.route("/404")
def error_404():
    return render_template("error/404.html")
