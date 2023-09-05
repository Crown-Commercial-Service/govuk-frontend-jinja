
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


def njk_template_from_string(env, source, globals=None, template_class=None):
    "A copy of Environment.from_string that we can use to convince jinja this is an .njk template"
    globals = env.make_globals(globals)
    cls = template_class or env.template_class
    return cls.from_code(env, env.compile(source, filename="foo.njk"), globals, None)


class TestEnvironment:
    def test_inline_cond_can_behave_like_jinja(self, env):
        template = env.from_string("{{ ('abc' if 2 > 3).strip() }}")

        with pytest.raises(jinja2.exceptions.UndefinedError, match=r"inline if-expression"):
            template.render()

    def test_inline_cond_can_behave_like_nunjucks(self, env):
        template = njk_template_from_string(env, "{{ ('abc' if 2 > 3).strip() }}")

        assert template.render() == ""


class TestStrictEquality:
    def test_jinja_raises_syntax_error_for_strict_equality_operator(self, env):
        with pytest.raises(jinja2.exceptions.TemplateSyntaxError, match="unexpected '='"):
            env.from_string("{% if 1 === 1 %}always true{% endif %}")

    def test_njk_has_strict_equality_operator(self, env):
        template = njk_template_from_string(env, "{% if 1 === 1 %}always true{% endif %}")

        assert template.render() == "always true"

    def test_strict_equality_operator(self, env):
        template = njk_template_from_string(env, "{% if var === true %}true if true{% endif %}")

        assert template.render(var=True) == "true if true"
        assert template.render(var=False) == ""
        assert template.render(var=1) == ""


class TestStrictInequality():
    def test_jinja_raises_syntax_error_for_strict_equality_operator(self, env):
        with pytest.raises(
            jinja2.exceptions.TemplateSyntaxError, match="unexpected '='"
        ):
            env.from_string("{% if 1 !== 1 %}always false{% endif %}")

    def test_njk_has_strict_equality_operator(self, env):
        template = njk_template_from_string(
            env, "{% if 1 !== '1' %}always true{% endif %}"
        )

        assert template.render() == "always true"

    def test_strict_equality_operator(self, env):
        template = njk_template_from_string(
            env, "{% if var !== true %}true if false{% endif %}"
        )

        assert template.render(var=True) == ""
        assert template.render(var=False) == "true if false"
        assert template.render(var=1) == "true if false"
