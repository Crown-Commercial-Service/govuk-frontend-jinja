
import pytest
from unittest import mock

import jinja2
from govuk_frontend.templates import NunjucksExtension


@pytest.fixture(autouse=True)
def njk_to_j2():
    with mock.patch("govuk_frontend.templates.njk_to_j2") as m:
        yield m


class TestExtension:
    @pytest.fixture
    def ext(self):
        return jinja2.Environment()

    def test_preprocesses_nunjucks_templates(self, env, njk_to_j2):
        ext = NunjucksExtension(env)
        assert ext.preprocess("foo", "bar", "baz.njk") == njk_to_j2("foo")

    def test_does_not_preprocess_jinja_templates(self, env, njk_to_j2):
        ext = NunjucksExtension(env)
        assert ext.preprocess("foo", "bar", "baz.j2") == "foo"
        assert njk_to_j2.call_count == 0

    def test_does_not_preprocess_template_from_memory(self, env, njk_to_j2):
        ext = NunjucksExtension(env)
        assert ext.preprocess("foo", "bar") == "foo"
        assert njk_to_j2.call_count == 0


class TestExtensionWithFileSystemLoader:
    @pytest.fixture
    def env(self, tmpdir):
        return jinja2.Environment(
            extensions=[NunjucksExtension],
            loader=jinja2.FileSystemLoader([tmpdir]),
        )

    def test_preprocesses_nunjucks_template(self, env, tmpdir, njk_to_j2):
        template_file = tmpdir.join("template.njk")
        template_file.write("foobar")
        env.get_template("template.njk")
        assert njk_to_j2.call_count == 1
        assert njk_to_j2.call_args == mock.call("foobar")


    def test_does_not_preprocess_jinja_templates(self, env, tmpdir, njk_to_j2):
        template_file = tmpdir.join("template.j2")
        template_file.write("foobar")
        env.get_template("template.j2")
        assert njk_to_j2.call_count == 0
