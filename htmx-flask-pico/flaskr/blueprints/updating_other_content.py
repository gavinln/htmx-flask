from flask import Blueprint, make_response, render_template, request

bp = Blueprint(
    "updating_other_content", __name__, url_prefix="/updating_other_content"
)


data = [
    {
        "name": "Joe Smith",
        "email": "joe@smith.org",
    },
    {
        "name": "Angie MacDowell",
        "email": "angie@macdowell.org",
    },
]


@bp.route("/")
def index():
    return render_template("updating_other_content/index.html", contacts=data)


@bp.route("/contacts1", methods=["POST"])
def contacts1():
    data.append(
        {
            "name": request.form["name"],
            "email": request.form["email"],
        }
    )
    return render_template(
        "updating_other_content/partial_1.html", contacts=data
    )


@bp.route("/contacts2", methods=["POST"])
def contacts2():
    contact = {
        "name": request.form["name"],
        "email": request.form["email"],
    }
    data.append(contact)
    return render_template(
        "updating_other_content/partial_2.html", contact=contact
    )


@bp.route("/contacts3", methods=["POST"])
def contacts3():
    data.append(
        {
            "name": request.form["name"],
            "email": request.form["email"],
        }
    )
    res = make_response(
        render_template("updating_other_content/partial_3.html")
    )
    res.headers["HX-Trigger"] = "newContact"
    return res


@bp.route("/contacts3/table")
def contacts3_table():
    return render_template(
        "updating_other_content/partial_3_table.html", contacts=data
    )
