import string
from math import floor
from random import random

from flask import Blueprint, make_response, render_template, request

bp = Blueprint("dialogs_browser", __name__, url_prefix="/dialogs_browser")


@bp.route("/")
def index():
    return render_template("dialogs_browser/index.html")


@bp.route("/submit", methods=["POST"])
def submit():
    response = request.headers["HX-Prompt"]
    return f"User entered <i>{response}</i>"
