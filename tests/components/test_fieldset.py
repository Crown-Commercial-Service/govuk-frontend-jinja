
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
