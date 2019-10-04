
from flask.templating import Environment as FlaskEnvironment
from govuk_frontend_jinja.templates import Environment as NunjucksEnvironment
from govuk_frontend_jinja.templates import NunjucksExtension, NunjucksUndefined, indent_njk


class Environment(FlaskEnvironment, NunjucksEnvironment):
    pass


def init_govuk_frontend(app):
    """Use the govuk_frontend_jinja Jinja environment in a Flask app

    >>> from flask import Flask
    >>> app = Flask("cheeseshop_service")
    >>> init_govuk_frontend(app)
    """
    app.jinja_environment = Environment
    jinja_options = app.jinja_options.copy()
    if "extensions" in jinja_options:
        jinja_options["extensions"].append(NunjucksExtension)
    else:
        jinja_options["extensions"] = [NunjucksExtension]
    jinja_options["undefined"] = NunjucksUndefined
    app.jinja_options = jinja_options
    app.add_template_filter(indent_njk)
    return app
