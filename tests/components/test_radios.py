
import pytest

from govuk_frontend.templates import Environment


@pytest.mark.xfail(reason="issue#4: template tries to set variable in outer scope")
def test_radios():
    env = Environment()
    template = env.from_string(
"""{% from "radios/macro.njk" import govukRadios %}

{{ govukRadios({
  "idPrefix": "example",
  "name": "example",
  "fieldset": {
    "legend": {
      "text": "Have you changed your name?"
    }
  },
  "hint": {
    "text": "This includes changing your last name or spelling your name differently."
  },
  "items": [
    {
      "value": "yes",
      "text": "Yes"
    },
    {
      "value": "no",
      "text": "No",
      "checked": true
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

  <fieldset class="govuk-fieldset" aria-describedby="example-hint">

  <legend class="govuk-fieldset__legend">
    Have you changed your name?
  </legend>

  <span id="example-hint" class="govuk-hint">
    This includes changing your last name or spelling your name differently.
  </span>

  <div class="govuk-radios">

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="example-1" name="example" type="radio" value="yes">
      <label class="govuk-label govuk-radios__label" for="example-1">
        Yes
      </label>
    </div>

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="example-2" name="example" type="radio" value="no" checked>
      <label class="govuk-label govuk-radios__label" for="example-2">
        No
      </label>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )


def test_radios_without_fieldset():
    env = Environment()
    template = env.from_string(
"""
{% from "radios/macro.njk" import govukRadios %}

{{ govukRadios({
  "name": "colours",
  "items": [
    {
      "value": "red",
      "text": "Red"
    },
    {
      "value": "green",
      "text": "Green"
    },
    {
      "value": "blue",
      "text": "Blue"
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

  <div class="govuk-radios">

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="colours-1" name="colours" type="radio" value="red">
      <label class="govuk-label govuk-radios__label" for="colours-1">
        Red
      </label>
    </div>

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="colours-2" name="colours" type="radio" value="green">
      <label class="govuk-label govuk-radios__label" for="colours-2">
        Green
      </label>
    </div>

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="colours-3" name="colours" type="radio" value="blue">
      <label class="govuk-label govuk-radios__label" for="colours-3">
        Blue
      </label>
    </div>

  </div>

</div>
"""
        ).strip()
    )
