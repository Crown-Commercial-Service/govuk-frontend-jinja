
import pytest


def test_select(env):
    template = env.from_string(
"""
{% from "select/macro.njk" import govukSelect %}

{{ govukSelect({
  "id": "select-1",
  "name": "select-1",
  "label": {
    "text": "Label text goes here"
  },
  "items": [
    {
      "value": 1,
      "text": "GOV.UK frontend option 1"
    },
    {
      "value": 2,
      "text": "GOV.UK frontend option 2",
      "selected": true
    },
    {
      "value": 3,
      "text": "GOV.UK frontend option 3",
      "disabled": true
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
  <label class="govuk-label" for="select-1">
    Label text goes here
  </label>

  <select class="govuk-select" id="select-1" name="select-1">

    <option value="1">GOV.UK frontend option 1</option>

    <option value="2" selected>GOV.UK frontend option 2</option>

    <option value="3" disabled>GOV.UK frontend option 3</option>

  </select>
</div>
"""
        )
    )
