from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    request,
    url_for,
)
from flask_login import (
    login_user,
    logout_user,
    current_user,
)
from .forms import (
    LoginForm,
    SignUpForm,
)
from .logics import (
    check_to_login,
    get_user_by_username,
    check_to_sign_up,
)
from app.packages.utils import is_url_safe

bp = Blueprint(
    name="authentication",
    import_name=__name__,
    template_folder="templates",
    url_prefix="/auth",
    static_folder="static",
)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = check_to_login(form)
        if user:
            nxt = request.args.get('next')
            login_user(
                user=user,
                remember=form.remember_me.data,
            )
            flash("[+] welcome %s" % current_user.username)
            if is_url_safe(nxt):
                return redirect(nxt)
            else:
                return redirect("/")
        else:
            flash("[-] Username & Password mixing is invalid.")
            return redirect(url_for('authentication.login'), )
    return render_template(
        "authentication/login.html",
        form=form,
    )


@bp.route("/logout", )
def logout():
    logout_user()
    flash("[+] logout successfully done.")
    return redirect(url_for("index"))


@bp.route("/<string:username>")
def user(username, ):
    user_obj = get_user_by_username(username=username)
    file_name = 'default_profile.jpg'
    return render_template("authentication/profile.html", user=user_obj, file_name=file_name)


@bp.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        check_to_sign_up(form)
        flash("[+] Sing up successfully done.")
        return redirect(url_for('authentication.login'))
    return render_template("authentication/signup.html", form=form)
