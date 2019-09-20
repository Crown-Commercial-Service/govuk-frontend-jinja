
import pytest


def test_warning_text(env):
    template = env.from_string(
"""
{% from "warning-text/macro.njk" import govukWarningText %}

{{ govukWarningText({
  "text": "You can be fined up to £5,000 if you don’t register.",
  "iconFallbackText": "Warning"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-warning-text">
  <span class="govuk-warning-text__icon" aria-hidden="true">!</span>
  <strong class="govuk-warning-text__text">
    <span class="govuk-warning-text__assistive">Warning</span>
    You can be fined up to £5,000 if you don’t register.
  </strong>
</div>
"""
        )
    )
