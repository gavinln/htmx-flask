import random
import string

from flask import Blueprint, render_template, request

bp = Blueprint("lazy_loading", __name__, url_prefix="/lazy_loading")


@bp.route("/")
def index():
    return render_template("lazy_loading/index.html")


@bp.route("/graph")
def graph():
    return render_template("lazy_loading/image.html")
