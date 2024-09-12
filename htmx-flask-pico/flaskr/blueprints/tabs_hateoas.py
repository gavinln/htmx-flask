import string
from math import floor
from random import random

from flask import Blueprint, make_response, render_template, request

bp = Blueprint("tabs_hateoas", __name__, url_prefix="/tabs_hateoas")


@bp.route("/")
def index():
    return render_template("tabs_hateoas/index.html")


@bp.route("/tab1/")
def tab1():
    return render_template("tabs_hateoas/tab1.html")


@bp.route("/tab2/")
def tab2():
    return render_template("tabs_hateoas/tab2.html")


@bp.route("/tab3/")
def tab3():
    return render_template("tabs_hateoas/tab3.html")
