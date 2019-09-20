
import pytest


def test_details(env):
    template = env.from_string(
"""
{% from "details/macro.njk" import govukDetails %}

{{ govukDetails({
  "summaryText": "Help with nationality",
  "text": "We need to know your nationality so we can work out which elections you’re entitled to vote in. If you can’t provide your nationality, you’ll have to send copies of identity documents through the post."
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
            """
            <details class="govuk-details">
              <summary class="govuk-details__summary">
                <span class="govuk-details__summary-text">
                  Help with nationality
                </span>
              </summary>
              <div class="govuk-details__text">
                We need to know your nationality so we can work out which elections you’re entitled to vote in. If you can’t provide your nationality, you’ll have to send copies of identity documents through the post.
              </div>
            </details>
            """
        )
    )


def test_details_with_html(env):
    template = env.from_string(
"""
{% from "details/macro.njk" import govukDetails %}

{{ govukDetails({
  "summaryText": "Where to find your National Insurance Number",
  "html": "Your National Insurance number can be found on\n<ul>\n  <li>your National Insurance card</li>\n  <li>your payslip</li>\n  <li>P60</li>\n  <li>benefits information</li>\n  <li>tax return</li>\n</ul>\n"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
            """
            <details class="govuk-details">
              <summary class="govuk-details__summary">
                <span class="govuk-details__summary-text">
                  Where to find your National Insurance Number
                </span>
              </summary>
              <div class="govuk-details__text">
                Your National Insurance number can be found on
            <ul>
              <li>your National Insurance card</li>
              <li>your payslip</li>
              <li>P60</li>
              <li>benefits information</li>
              <li>tax return</li>
            </ul>

              </div>
            </details>
            """
        )
    )
