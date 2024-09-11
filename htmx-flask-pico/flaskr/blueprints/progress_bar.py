import string
from math import floor
from random import random

from flask import Blueprint, make_response, render_template, request

bp = Blueprint("progress_bar", __name__, url_prefix="/progress_bar")

percentage = 0


@bp.route("/")
def index():
    return render_template("progress_bar/index.html")


@bp.route("/start", methods=["POST"])
def start():
    global percentage
    percentage = 0
    return render_template(
        "progress_bar/in_progress.html", percentage=0, complete=False
    )


@bp.route("/job")
def job():
    return render_template(
        "progress_bar/in_progress.html",
        percentage=percentage,
        complete=percentage >= 100,
    )


@bp.route("/job/progress")
def progress():
    global percentage
    percentage += floor(33 * random())
    res = make_response(
        render_template(
            "progress_bar/progress_bar.html",
            percentage=percentage,
            complete=percentage >= 100,
        )
    )
    # the header triggers "hx-trigger" which calls /progress_bar/job
    res.headers.set("HX-Trigger", "done")
    return res
