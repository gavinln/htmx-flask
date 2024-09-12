import string
from math import floor
from random import random

from flask import Blueprint, make_response, render_template, request

bp = Blueprint("value_select", __name__, url_prefix="/value_select")


data = {
    "audi": {"models": ["A1", "A4", "A6"]},
    "toyota": {"models": ["Landcruiser", "Tacoma", "Yaris"]},
    "bmw": {"models": ["325i", "325ix", "X5"]},
}


@bp.route("/")
def index():
    current_make = "audi"
    return render_template(
        "value_select/index.html",
        makes=data.keys(),
        current_make=current_make,
        models=data[current_make]["models"],
    )


@bp.route("/models/")
def models():
    current_make = request.args["make"]
    return render_template(
        "value_select/partial_models.html",
        makes=data.keys(),
        current_make=current_make,
        models=data[current_make]["models"],
    )
