
from govuk_frontend.templates import Environment


def test_input():
    env = Environment()
    template = env.from_string(
"""
{% from "input/macro.njk" import govukInput %}

{{ govukInput({
  "label": {
    "text": "National Insurance number"
  },
  "id": "input-example",
  "name": "test-name"
}) }}
"""
    )
    assert (
        template.render()
        ==
"""\n\n\n\n
<div class="govuk-form-group">
  <label class="govuk-label" for="input-example">
    National Insurance number
  </label>


  <input class="govuk-input" id="input-example" name="test-name" type="text">
</div>"""
    )
