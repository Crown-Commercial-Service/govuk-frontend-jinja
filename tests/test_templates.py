
import pytest

import govuk_frontend.templates


def test_environment_contains_govuk_frontend_templates_which_can_be_rendered():
    env = govuk_frontend.templates.Environment()
    template = env.get_template("template.njk")
    assert template.render()
