import string
import random

from flask import Blueprint, render_template, request

bp = Blueprint("click_to_load", __name__, url_prefix="/click_to_load")


def generate_contacts(page=1, page_size=5):
    def generate_contact(i):
        def generate_id(n=10):
            return "".join(
                random.choices(string.ascii_uppercase + string.digits, k=n)
            )

        contact_id = (page - 1) * page_size + (i + 1)
        return {
            "name": "Agent Smith",
            "email": f"void{contact_id}@null.org",
            "id": generate_id(),
        }

    return [generate_contact(i) for i in range(page_size)]


@bp.route("/", defaults={"page": 1})
def index(page):
    contacts = generate_contacts(page=page)
    return render_template(
        "click_to_load/index.html", contacts=contacts, page=page
    )


@bp.route("/more_rows/")
def more_rows():
    page = int(request.args.get("page", 1))
    return render_template(
        "click_to_load/more-rows.html",
        contacts=generate_contacts(page=page),
        page=page,
    )
