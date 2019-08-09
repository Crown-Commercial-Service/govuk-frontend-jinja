
import pytest

from govuk_frontend.templates import Environment


def test_fieldset():
    env = Environment()
    template = env.from_string(
"""{% from "components/fieldset/macro.njk" import govukFieldset %}

{{ govukFieldset({
  "legend": {
    "text": "What is your address?"
  }
}) }}
"""
    )
    assert (
        template.render()
        ==
"""

<fieldset class="govuk-fieldset">
  
  <legend class="govuk-fieldset__legend">
    What is your address?
  </legend>
  
</fieldset>"""
    )


def test_fieldset_with_block():
    env = Environment()
    template = env.from_string(
"""
{% from "components/fieldset/macro.njk" import govukFieldset %}

{% call govukFieldset({
  "legend": {
    "text": "What is your address?"
  }
}) %}
  <div class="govuk-form-group">
    <label class="govuk-label" for="address-line-1">
      Building and street <span class="govuk-visually-hidden">line 1 of 2</span>
    </label>
    <input class="govuk-input" id="address-line-1" name="address-line-1" type="text">
  </div>
{% endcall %}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<fieldset class="govuk-fieldset">

  <legend class="govuk-fieldset__legend">
    What is your address?
  </legend>

  <div class="govuk-form-group">
    <label class="govuk-label" for="address-line-1">
      Building and street <span class="govuk-visually-hidden">line 1 of 2</span>
    </label>
    <input class="govuk-input" id="address-line-1" name="address-line-1" type="text">
  </div>
</fieldset>
"""
        )
    )
