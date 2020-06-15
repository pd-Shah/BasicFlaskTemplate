from flask import (
    Blueprint,
    render_template,
)
from flask_login import login_required
from app.packages.authentication.logics import permission_required
from app.packages.authentication.models import Permission

bp = Blueprint(
    "admin",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/admin",
)


@bp.route("/")
@login_required
@permission_required(Permission.ADMIN)
def index():
    return render_template('admin/index.html')
