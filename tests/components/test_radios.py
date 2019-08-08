
from govuk_frontend.templates import Environment


def test_radios():
    env = Environment()
    template = env.from_string(
"""{% from "components/radios/macro.njk" import govukRadios %}

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
        template.render()
        ==
"""

<fieldset class="govuk-fieldset">
  
  <legend class="govuk-fieldset__legend">
    What is your address?
  </legend>
  
</fieldset>"""
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
