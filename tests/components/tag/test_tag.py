
import pytest


def test_tag(env):
    template = env.from_string(
"""
{% from "tag/macro.njk" import govukTag %}

{{ govukTag({
  "text": "alpha"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<strong class="govuk-tag">
  alpha
</strong>
"""
        )
    )


def test_tag_inactive(env):
    template = env.from_string(
"""
{% from "tag/macro.njk" import govukTag %}

{{ govukTag({
  "text": "alpha",
  "classes": "govuk-tag--inactive"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<strong class="govuk-tag govuk-tag--inactive">
  alpha
</strong>
"""
        )
    )
