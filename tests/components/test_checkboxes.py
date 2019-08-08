
import pytest

from govuk_frontend.templates import Environment


@pytest.mark.xfail(reason="issue#4: template tries to set variable in outer scope")
def test_checkboxes():
    env = Environment()
    template = env.from_string(
"""
{% from "checkboxes/macro.njk" import govukCheckboxes %}

{{ govukCheckboxes({
  "idPrefix": "nationality",
  "name": "nationality",
  "fieldset": {
    "legend": {
      "text": "What is your nationality?"
    }
  },
  "hint": {
    "text": "If you have dual nationality, select all options that are relevant to you."
  },
  "items": [
    {
      "value": "british",
      "text": "British"
    },
    {
      "value": "irish",
      "text": "Irish"
    },
    {
      "value": "other",
      "text": "Citizen of another country"
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
<div class="govuk-form-group">

  <fieldset class="govuk-fieldset" aria-describedby="nationality-hint">

  <legend class="govuk-fieldset__legend">
    What is your nationality?
  </legend>

  <span id="nationality-hint" class="govuk-hint">
    If you have dual nationality, select all options that are relevant to you.
  </span>

  <div class="govuk-checkboxes">

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="nationality-1" name="nationality" type="checkbox" value="british">
      <label class="govuk-label govuk-checkboxes__label" for="nationality-1">
        British
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="nationality-2" name="nationality" type="checkbox" value="irish">
      <label class="govuk-label govuk-checkboxes__label" for="nationality-2">
        Irish
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="nationality-3" name="nationality" type="checkbox" value="other">
      <label class="govuk-label govuk-checkboxes__label" for="nationality-3">
        Citizen of another country
      </label>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )
