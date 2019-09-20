
import pytest


def test_panel(env):
    template = env.from_string(
"""
{% from "panel/macro.njk" import govukPanel %}

{{ govukPanel({
  "titleHtml": "Application complete",
  "text": "Your reference number: HDJ2123F"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-panel govuk-panel--confirmation">
  <h1 class="govuk-panel__title">
    Application complete
  </h1>

  <div class="govuk-panel__body">
    Your reference number: HDJ2123F
  </div>

</div>
"""
        )
    )


def test_panel_custom_heading_level(env):
    template = env.from_string(
"""
{% from "panel/macro.njk" import govukPanel %}

{{ govukPanel({
  "titleText": "Application complete",
  "headingLevel": 2,
  "text": "Your reference number: HDJ2123F"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-panel govuk-panel--confirmation">
  <h2 class="govuk-panel__title">
    Application complete
  </h2>

  <div class="govuk-panel__body">
    Your reference number: HDJ2123F
  </div>

</div>
"""
        )
    )
