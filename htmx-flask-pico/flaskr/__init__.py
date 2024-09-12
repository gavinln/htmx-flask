from flask import Flask, render_template
from jinja2 import StrictUndefined

from .blueprints import (
    active_search,
    bulk_update,
    click_to_edit,
    click_to_load,
    delete_row,
    dialogs_pico,
    edit_row,
    infinite_scroll,
    inline_validation,
    lazy_loading,
    progress_bar,
    value_select,
    tabs_hateoas,
)


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
app.register_blueprint(bulk_update.bp)
app.register_blueprint(click_to_load.bp)
app.register_blueprint(delete_row.bp)
app.register_blueprint(edit_row.bp)
app.register_blueprint(lazy_loading.bp)
app.register_blueprint(inline_validation.bp)
app.register_blueprint(infinite_scroll.bp)
app.register_blueprint(active_search.bp)
app.register_blueprint(progress_bar.bp)
app.register_blueprint(value_select.bp)
app.register_blueprint(dialogs_pico.bp)
app.register_blueprint(tabs_hateoas.bp)


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="HTMX-Flask-Pico",
        text="Click on the left menu",
    )


@app.route("/html5_test")
def html5_test():
    return render_template("html5-test.html")


@app.route("/pico_containers")
def pico_containers():
    return render_template("pico-containers.html")


@app.route("/pico_examples")
@app.route("/pico_examples/<page>")
def pico_examples(page=None):
    if not page:
        page = "typography"
    template_name = "pico-examples/{}.html".format(page)
    print(template_name)
    return render_template(template_name)
