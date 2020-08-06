import pytest

pytestmark = pytest.mark.skipif(
    pytest.helpers.govuk_frontend_version_info() < (2, 5),
    reason="requires govuk-frontend >= 2.5",
)


def test_summary_list(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_with_actions(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_with_some_actions(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_without_actions(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_summary_list_without_borders(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
