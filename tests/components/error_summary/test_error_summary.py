
import pytest


def test_error_summary(env):
    template = env.from_string(
"""
{% from "error-summary/macro.njk" import govukErrorSummary %}

{{ govukErrorSummary({
  "titleText": "Message to alert the user to a problem goes here",
  "descriptionText": "Optional description of the errors and how to correct them",
  "classes": "optional-extra-class",
  "errorList": [
    {
      "text": "Descriptive link to the question with an error",
      "href": "#example-error-1"
    },
    {
      "text": "Descriptive link to the question with an error",
      "href": "#example-error-1"
    }
  ]
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-error-summary optional-extra-class" aria-labelledby="error-summary-title" role="alert" tabindex="-1" data-module="error-summary">
  <h2 class="govuk-error-summary__title" id="error-summary-title">
    Message to alert the user to a problem goes here
  </h2>
  <div class="govuk-error-summary__body">

    <p>
      Optional description of the errors and how to correct them
    </p>

    <ul class="govuk-list govuk-error-summary__list">

      <li>

        <a href="#example-error-1">Descriptive link to the question with an error</a>

      </li>

      <li>

        <a href="#example-error-1">Descriptive link to the question with an error</a>

      </li>

    </ul>
  </div>
</div>
"""
        )
    )
