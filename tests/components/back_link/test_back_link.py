
import pytest


def test_back_link(env):
    template = env.from_string(
"""
{% from "back-link/macro.njk" import govukBackLink %}

{{ govukBackLink({
  "href": "#"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<a href="#" class="govuk-back-link">Back</a>
"""
        )
    )


def test_back_link_with_custom_text(env):
    template = env.from_string(
"""
{% from "back-link/macro.njk" import govukBackLink %}

{{ govukBackLink({
  "href": "#",
  "text": "Back to home"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<a href="#" class="govuk-back-link">Back to home</a>
"""
        )
    )
