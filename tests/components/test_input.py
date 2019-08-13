
import pytest

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


def test_input_with_hint_text():
    env = Environment()
    template = env.from_string(
r"""
{% from "input/macro.njk" import govukInput %}

{{ govukInput({
  "label": {
    "text": "National insurance number"
  },
  "hint": {
    "text": "It’s on your National Insurance card, benefit letter, payslip or P60\. For example, ‘QQ 12 34 56 C’."
  },
  "id": "input-with-hint-text",
  "name": "test-name-2"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
r"""
<div class="govuk-form-group">
  <label class="govuk-label" for="input-with-hint-text">
    National insurance number
  </label>

  <span id="input-with-hint-text-hint" class="govuk-hint">
    It’s on your National Insurance card, benefit letter, payslip or P60\. For example, ‘QQ 12 34 56 C’.
  </span>

  <input class="govuk-input" id="input-with-hint-text" name="test-name-2" type="text" aria-describedby="input-with-hint-text-hint">
</div>
"""
        )
    )


def test_input_with_error_mesage():
    env = Environment()
    template = env.from_string(
r"""
{% from "input/macro.njk" import govukInput %}

{{ govukInput({
  "label": {
    "text": "National Insurance number"
  },
  "hint": {
    "text": "It’s on your National Insurance card, benefit letter, payslip or P60\. For example, ‘QQ 12 34 56 C’."
  },
  "id": "input-with-error-message",
  "name": "test-name-3",
  "errorMessage": {
    "text": "Error message goes here"
  }
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
            r"""
            <div class="govuk-form-group govuk-form-group--error">
              <label class="govuk-label" for="input-with-error-message">
                National Insurance number
              </label>

              <span id="input-with-error-message-hint" class="govuk-hint">
                It’s on your National Insurance card, benefit letter, payslip or P60\. For example, ‘QQ 12 34 56 C’.
              </span>

              <span id="input-with-error-message-error" class="govuk-error-message">
                Error message goes here
              </span>

              <input class="govuk-input govuk-input--error" id="input-with-error-message" name="test-name-3" type="text" aria-describedby="input-with-error-message-hint input-with-error-message-error">
            </div>
            """
        )
    )


def test_input_with_attributes():
    env = Environment()
    template = env.from_string(
"""
{% from "input/macro.njk" import govukInput %}

{{ govukInput({
  "label": {
    "text": "Number"
  },
  "id": "input-example",
  "name": "test-name",
  "attributes": {
    "pattern": "[0-9]*",
  },
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-form-group">
  <label class="govuk-label" for="input-example">
    Number
  </label>

  <input class="govuk-input" id="input-example" name="test-name" type="text" pattern="[0-9]*">
</div>
"""
        )
    )
