
import pytest


@pytest.mark.xfail(reason="tests with html causing lexer errors")
def test_phase_banner(env):
    template = env.from_string(
"""
{% from "phase-banner/macro.njk" import govukPhaseBanner %}

{{ govukPhaseBanner({
  "tag": {
    "text": "alpha"
  },
  "html": "This is a new service - your <a href=\"#\" class=\"govuk-link\">feedback</a> will help us to improve it."
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-phase-banner">
  <p class="govuk-phase-banner__content"><strong class="govuk-tag govuk-phase-banner__content__tag ">
  alpha
</strong>
<span class="govuk-phase-banner__text">
      This is a new service - your <a href="#" class="govuk-link">feedback</a> will help us to improve it.
    </span>
  </p>
</div>
"""
        )
    )


def test_phase_banner_with_text(env):
    template = env.from_string(
"""
{% from "phase-banner/macro.njk" import govukPhaseBanner %}

{{ govukPhaseBanner({
  "tag": {
    "text": "alpha"
  },
  "text": "This is a new service - your feedback will help us to improve it."
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-phase-banner">
  <p class="govuk-phase-banner__content"><strong class="govuk-tag govuk-phase-banner__content__tag ">
  alpha
</strong><span class="govuk-phase-banner__text">
      This is a new service - your feedback will help us to improve it.
    </span>
  </p>
</div>
"""
        )
    )
