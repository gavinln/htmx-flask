import random
import string

from flask import Blueprint, render_template, request

bp = Blueprint("edit_row", __name__, url_prefix="/edit_row")

data = {
    0: {
        "name": "Joe Smith",
        "email": "joe@smith.org",
    },
    1: {
        "name": "Angie MacDowell",
        "email": "angie@macdowell.org",
    },
    2: {
        "name": "Fuqua Tarkenton",
        "email": "fuqua@tarkenton.org",
    },
    3: {
        "name": "Kim Yee",
        "email": "kim@yee.org",
    },
}


@bp.route("/")
def index():
    return render_template("edit_row/index.html", contacts=data)


@bp.route("/contact/<int:id>/edit", methods=["GET", "PUT"])
def contact_edit(id):
    if request.method == "PUT":
        id = request.form.get("id")
        name = request.form.get("name")
        data[int(id)]["name"] = name  # type: ignore
        return render_template("edit_row/index.html", contacts=data)

    return render_template("edit_row/edit_row.html", contacts=data, id=id)
