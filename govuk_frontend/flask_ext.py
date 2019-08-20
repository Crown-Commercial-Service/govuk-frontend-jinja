
from flask.templating import Environment as FlaskEnvironment
from govuk_frontend.templates import Environment as NunjucksEnvironment
from govuk_frontend.templates import NunjucksExtension, NunjucksUndefined


class Environment(FlaskEnvironment, NunjucksEnvironment):
    pass


def init_govuk_frontend(app):
    """Use the govuk_frontend Jinja environment in a Flask app

    >>> from flask import Flask
    >>> app = Flask("cheeseshop_service")
    >>> init_govuk_frontend(app)
    """
    app.jinja_environment = Environment
    app.jinja_options["extensions"].append(NunjucksExtension)
    app.jinja_options["undefined"] = NunjucksUndefined
    return app
