import string
from math import floor
from random import random

from flask import Blueprint, make_response, render_template, request

bp = Blueprint("dialogs_pico", __name__, url_prefix="/dialogs_pico")


@bp.route("/")
def index():
    return render_template("dialogs_pico/index.html")


@bp.route("/modal/")
def models():
    return render_template("dialogs_pico/modal.html")
