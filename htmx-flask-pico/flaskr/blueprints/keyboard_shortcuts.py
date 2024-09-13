import string
import random

from flask import Blueprint, render_template, request

bp = Blueprint(
    "keyboard_shortcuts", __name__, url_prefix="/keyboard_shortcuts"
)


@bp.route("/")
def index():
    return render_template("keyboard_shortcuts/index.html")


@bp.route("/doit", methods=["POST"])
def doit():
    return "Did it!"
