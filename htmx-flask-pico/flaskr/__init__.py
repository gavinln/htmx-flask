from flask import Flask, render_template
from jinja2 import StrictUndefined

from .blueprints import click_to_edit


def initialize_app(app, test_config=None):
    app.config.from_mapping(
        SECRET_KEY="dev",
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    return app


app = Flask(__name__, instance_relative_config=True)
app = initialize_app(app)

# throws an exception for undefined variable in Jinja template
app.jinja_env.undefined = StrictUndefined

app.register_blueprint(click_to_edit.bp)


@app.route("/")
def index():
    return render_template("index.html", title="Hello", text="Hello, World!")


@app.route("/html5_test")
def html5_test():
    return render_template("html5-test.html")
