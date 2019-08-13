
import pytest

import jinja2
from govuk_frontend.templates import Environment, NunjucksUndefined


def test_environment_contains_govuk_frontend_templates_which_can_be_rendered():
    env = Environment()
    template = env.get_template("template.njk")
    assert template.render()


class TestNunjucksUndefined:
    
    @pytest.fixture
    def env(self):
        return jinja2.Environment(undefined=NunjucksUndefined)

    def test_undefined_is_chainable(self, env):
        template = env.from_string("{{ item.hint.text }}")
        assert (
            template.render(item={"hint": {"text": "foobar"}})
            ==
            "foobar"
        )
        assert (
            template.render(item={"hint": {}})
            ==
            ""
        )
        assert (
            template.render(item={})
            ==
            ""
        )
        assert (
            template.render()
            ==
            ""
        )
