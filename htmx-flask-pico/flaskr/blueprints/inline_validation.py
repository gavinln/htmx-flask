import random
import string

from flask import Blueprint, render_template, request

bp = Blueprint("inline_validation", __name__, url_prefix="/inline_validation")


def is_valid_email(email):
    return email == "test@test.com"


@bp.route("/")
def index():
    return render_template("inline_validation/index.html")


@bp.route("/contact/email", methods=["POST"])
def contact_email():
    email = request.form["email"]
    print(email)
    if not is_valid_email(email):
        return render_template(
            "inline_validation/partial_error.html", email=email
        )
    return render_template("inline_validation/partial_valid.html", email=email)
