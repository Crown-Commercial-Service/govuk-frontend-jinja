
import pytest


@pytest.mark.xfail(reason="inline if-expression not targeted by regex")
def test_character_count(env):
    template = env.from_string(
"""
{% from "character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  "name": "more-detail",
  "id": "more-detail",
  "maxlength": 10,
  "label": {
    "text": "Can you provide more detail?"
  }
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-character-count" data-module="character-count" data-maxlength="10">

<div class="govuk-form-group">
  <label class="govuk-label" for="more-detail">
    Can you provide more detail?
  </label>

  <textarea class="govuk-textarea js-character-count " id="more-detail" name="more-detail" rows="5"></textarea>
</div>

  <span id="more-detail-info" class="govuk-hint govuk-character-count__message" aria-live="polite">
    You can enter up to 10 characters
  </span>
</div>
"""
        )
    )


@pytest.mark.xfail(reason="inline if-expression not targeted by regex")
def test_character_count_with_hint(env):
    template = env.from_string(
"""
{% from "character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  "name": "with-hint",
  "id": "with-hint",
  "maxlength": 10,
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
<div class="govuk-character-count" data-module="character-count" data-maxlength="10">

<div class="govuk-form-group">
  <label class="govuk-label" for="with-hint">
    Can you provide more detail?
  </label>

  <span id="with-hint-hint" class="govuk-hint">
    Don&#39;t include personal or financial information, eg your National Insurance number or credit card details.
  </span>

  <textarea class="govuk-textarea js-character-count " id="with-hint" name="with-hint" rows="5" aria-describedby="with-hint-hint"></textarea>
</div>

  <span id="with-hint-info" class="govuk-hint govuk-character-count__message" aria-live="polite">
    You can enter up to 10 characters
  </span>
</div>
"""
        )
    )


@pytest.mark.xfail(reason="inline if-expression not targeted by regex")
def test_character_count_with_default_value(env):
    template = env.from_string(
"""
{% from "character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  "id": "with-default-value",
  "name": "default-value",
  "maxlength": 100,
  "label": {
    "text": "Full address"
  },
  "value": "221B Baker Street\nLondon\nNW1 6XE\n"
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-character-count" data-module="character-count" data-maxlength="100">

<div class="govuk-form-group">
  <label class="govuk-label" for="with-default-value">
    Full address
  </label>

  <textarea class="govuk-textarea js-character-count " id="with-default-value" name="default-value" rows="5">221B Baker Street
London
NW1 6XE
</textarea>
</div>

  <span id="with-default-value-info" class="govuk-hint govuk-character-count__message" aria-live="polite">
    You can enter up to 100 characters
  </span>
</div>
"""
        )
    )


def test_character_count_with_default_value_exceeding_limit(env):
    template = env.from_string(
"""
{% from "character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  "id": "exceeding-characters",
  "name": "exceeding",
  "maxlength": 10,
  "value": "221B Baker Street\nLondon\nNW1 6XE\n",
  "label": {
    "text": "Full address"
  },
  "errorMessage": {
    "text": "Please do not exceed the maximum allowed limit"
  }
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-character-count" data-module="character-count" data-maxlength="10">

<div class="govuk-form-group govuk-form-group--error">
  <label class="govuk-label" for="exceeding-characters">
    Full address
  </label>

  <span id="exceeding-characters-error" class="govuk-error-message">
    Please do not exceed the maximum allowed limit
  </span>

  <textarea class="govuk-textarea govuk-textarea--error js-character-count  govuk-textarea--error" id="exceeding-characters" name="exceeding" rows="5" aria-describedby="exceeding-characters-error">221B Baker Street
London
NW1 6XE
</textarea>
</div>

  <span id="exceeding-characters-info" class="govuk-hint govuk-character-count__message" aria-live="polite">
    You can enter up to 10 characters
  </span>
</div>
"""
        )
    )


@pytest.mark.xfail(reason="inline if-expression not targeted by regex")
def test_charcter_count_with_custom_rows(env):
    template = env.from_string(
"""
{% from "character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  "id": "custom-rows",
  "name": "custom",
  "maxlength": 10,
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
<div class="govuk-character-count" data-module="character-count" data-maxlength="10">

<div class="govuk-form-group">
  <label class="govuk-label" for="custom-rows">
    Full address
  </label>

  <textarea class="govuk-textarea js-character-count " id="custom-rows" name="custom" rows="8"></textarea>
</div>

  <span id="custom-rows-info" class="govuk-hint govuk-character-count__message" aria-live="polite">
    You can enter up to 10 characters
  </span>
</div>
"""
        )
    )


@pytest.mark.xfail(reason="inline if-expression not targeted by regex")
def test_character_count_with_label_as_page_heading(env):
    template = env.from_string(
"""
{% from "character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  "id": "textarea-with-page-heading",
  "name": "address",
  "maxlength": 10,
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
<div class="govuk-character-count" data-module="character-count" data-maxlength="10">

<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label" for="textarea-with-page-heading">
      Full address
    </label>

  </h1>

  <textarea class="govuk-textarea js-character-count " id="textarea-with-page-heading" name="address" rows="5"></textarea>
</div>

  <span id="textarea-with-page-heading-info" class="govuk-hint govuk-character-count__message" aria-live="polite">
    You can enter up to 10 characters
  </span>
</div>
"""
        )
    )


@pytest.mark.xfail(reason="inline if-expression not targeted by regex")
def test_character_count_with_word_count(env):
    template = env.from_string(
"""
{% from "character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  "id": "word-count",
  "name": "word-count",
  "maxwords": 10,
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
<div class="govuk-character-count" data-module="character-count" data-maxwords="10">

<div class="govuk-form-group">
  <label class="govuk-label" for="word-count">
    Full address
  </label>

  <textarea class="govuk-textarea js-character-count " id="word-count" name="word-count" rows="5"></textarea>
</div>

  <span id="word-count-info" class="govuk-hint govuk-character-count__message" aria-live="polite">
    You can enter up to 10 words
  </span>
</div>
"""
        )
    )


@pytest.mark.xfail(reason="inline if-expression not targeted by regex")
def test_character_count_with_threshold(env):
    template = env.from_string(
"""
{% from "character-count/macro.njk" import govukCharacterCount %}

{{ govukCharacterCount({
  "id": "with-threshold",
  "name": "with-threshold",
  "maxlength": 10,
  "threshold": 75,
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
<div class="govuk-character-count" data-module="character-count" data-maxlength="10" data-threshold="75">

<div class="govuk-form-group">
  <label class="govuk-label" for="with-threshold">
    Full address
  </label>

  <textarea class="govuk-textarea js-character-count " id="with-threshold" name="with-threshold" rows="5"></textarea>
</div>

  <span id="with-threshold-info" class="govuk-hint govuk-character-count__message" aria-live="polite">
    You can enter up to 10 characters
  </span>
</div>
"""
        )
    )
