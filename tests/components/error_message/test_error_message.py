
import pytest


def test_error_message(env):
    template = env.from_string(
"""
{% from "error-message/macro.njk" import govukErrorMessage %}

{{ govukErrorMessage({
  "text": "Error message about full name goes here"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<span class="govuk-error-message">
  Error message about full name goes here
</span>
"""
        )
    )
