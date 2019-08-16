
import pytest

from flask import Flask, render_template

import govuk_frontend
from govuk_frontend.flask_ext import Environment, init_govuk_frontend


@pytest.fixture
def app():
    return Flask("test_flask_ext")


def test_environment_takes_app_as_first_argument(app):
    env = Environment(app)
    assert env.app == app


def test_init_govuk_frontend(app):
    init_govuk_frontend(app)
    env = app.jinja_env

    assert (
        env.undefined
        ==
        govuk_frontend.templates.NunjucksUndefined
    )
    assert (
        "govuk_frontend.templates.NunjucksExtension"
        in
        env.extensions
    )


def test_render_template(app, loader):
    init_govuk_frontend(app)
    app.jinja_loader = loader

    with app.app_context():
        render_template("template.njk")
