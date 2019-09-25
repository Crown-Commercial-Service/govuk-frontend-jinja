import pytest

pytestmark = pytest.mark.skipif(
    pytest.helpers.govuk_frontend_version_info() < (2, 5),
    reason="requires govuk-frontend >= 2.5",
)


def test_accordion(env, template, expected, similar):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_with_additional_descriptions(env, template, expected, similar):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_with_one_section_open(env, template, expected, similar):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_accordion_with_all_sections_already_open(env, template, expected, similar):
    template = env.from_string(template)
    assert similar(template.render(), expected)
