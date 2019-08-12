
import pytest


@pytest.mark.xfail(reason="apostrophe not escaped")
def test_textarea(env):
    template = env.from_string(
"""
{% from "textarea/macro.njk" import govukTextarea %}

{{ govukTextarea({
  "name": "more-detail",
  "id": "more-detail",
  "label": {
    "text": "Can you provide more detail?"
  },
  "hint": {
    "text": "Don't include personal or financial information, eg your National Insurance number or credit card details."
  }
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-form-group">
  <label class="govuk-label" for="more-detail">
    Can you provide more detail?
  </label>

  <span id="more-detail-hint" class="govuk-hint">
    Don&#39;t include personal or financial information, eg your National Insurance number or credit card details.
  </span>

  <textarea class="govuk-textarea" id="more-detail" name="more-detail" rows="5" aria-describedby="more-detail-hint"></textarea>
</div>
"""
        )
    )


def test_textarea_with_default_value(env):
    template = env.from_string(
"""
{% from "textarea/macro.njk" import govukTextarea %}

{{ govukTextarea({
  "id": "full-address",
  "name": "address",
  "value": "221B Baker Street\nLondon\nNW1 6XE\n",
  "label": {
    "text": "Full address"
  }
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-form-group">
  <label class="govuk-label" for="full-address">
    Full address
  </label>

  <textarea class="govuk-textarea" id="full-address" name="address" rows="5">221B Baker Street
London
NW1 6XE
</textarea>
</div>
"""
        )
    )


def test_textarea_with_custom_rows(env):
    template = env.from_string(
"""
{% from "textarea/macro.njk" import govukTextarea %}

{{ govukTextarea({
  "id": "full-address",
  "name": "address",
  "label": {
    "text": "Full address"
  },
  "rows": 8
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-form-group">
  <label class="govuk-label" for="full-address">
    Full address
  </label>

  <textarea class="govuk-textarea" id="full-address" name="address" rows="8"></textarea>
</div>
"""
        )
    )


@pytest.mark.xfail(reason="autoescape required, HTML entities being escaped")
def test_textarea_with_label_as_page_heading(env):
    template = env.from_string(
"""
{% from "textarea/macro.njk" import govukTextarea %}

{{ govukTextarea({
  "id": "textarea-with-page-heading",
  "name": "address",
  "label": {
    "text": "Full address",
    "isPageHeading": true
  }
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label" for="textarea-with-page-heading">
      Full address
    </label>

  </h1>

  <textarea class="govuk-textarea" id="textarea-with-page-heading" name="address" rows="5"></textarea>
</div>
"""
        )
    )
