
from govuk_frontend.templates import Environment


def test_environment_contains_govuk_frontend_templates_which_can_be_rendered():
    env = Environment()
    template = env.get_template("template.njk")
    assert template.render()
