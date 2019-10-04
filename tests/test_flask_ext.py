
import pytest

flask = pytest.importorskip("flask", reason="requires Flask")

import jinja2

import govuk_frontend_jinja
from govuk_frontend_jinja.flask_ext import Environment, init_govuk_frontend

@pytest.fixture
def app(loader):
    app = flask.Flask("test_flask_ext")
    init_govuk_frontend(app)
    app.jinja_loader = loader
    return app


def test_environment_takes_app_as_first_argument():
    app = flask.Flask("test_flask_ext")
    env = Environment(app)
    assert env.app == app


def test_init_govuk_frontend(app):
    env = app.jinja_env

    assert (
        env.undefined
        ==
        govuk_frontend_jinja.templates.NunjucksUndefined
    )
    assert (
        "govuk_frontend_jinja.templates.NunjucksExtension"
        in
        env.extensions
    )
    assert "indent_njk" in env.filters


def test_render_template(app):
    with app.app_context():
        flask.render_template("template.njk")


def test_autoescape_is_enabled_for_njk_files_by_default(app):
    loader = jinja2.DictLoader({"test.njk": "{{ text }}"})
    app.jinja_loader = loader

    with app.app_context():
        assert flask.render_template("test.njk", text="<script>") == "&lt;script&gt;"


def test_autoescape_can_be_disabled(app):
    loader = jinja2.DictLoader({"test.njk": "{% autoescape on %}{{ text }}{% endautoescape %}"})
    app.jinja_loader = loader

    with app.app_context():
        assert flask.render_template("test.njk", text="<script>") == "<script>"
