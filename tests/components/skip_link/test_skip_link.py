
import pytest


def test_skip_link(env):
    template = env.from_string(
"""
{% from "skip-link/macro.njk" import govukSkipLink %}

{{ govukSkipLink({
  "text": "Skip to main content",
  "href": "#content"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<a href="#content" class="govuk-skip-link">Skip to main content</a>
"""
        )
    )
