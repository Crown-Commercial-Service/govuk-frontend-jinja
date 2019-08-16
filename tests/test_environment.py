
import pytest

import jinja2
from govuk_frontend_jinja.templates import Environment, NunjucksUndefined


def test_environment_contains_govuk_frontend_templates_which_can_be_rendered(env):
    template = env.get_template("template.njk")
    assert template.render()


class TestJoinPath:

    @pytest.fixture
    def env(self):
        return Environment(
            loader=jinja2.DictLoader({
                "a/a/a.njk": "{% include './b.njk' %}",
                "a/a/b.njk": "b",
                "a/b/b.njk": "{% include '../a/b.njk' %}",
                "c/c.html": "{% include 'a/a/a.njk' %}",
            })
        )

    def test_join_path_joins_relative_paths(self, env):
        template = env.get_template("a/a/a.njk")
        assert template.render() == "b"

        template = env.get_template("a/b/b.njk")
        assert template.render() == "b"

    def test_join_path_does_not_join_unanchored_paths(self, env):
        template = env.get_template("c/c.html")
        assert template.render() == "b"


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
