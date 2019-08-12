
import pytest

from govuk_frontend.templates import Environment


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


@pytest.mark.xfail(reason="Jinja undefined is stricter than Nunjucks undefined")
def test_checkboxes_with_id_and_name(env):
    template = env.from_string(
"""
{% from "checkboxes/macro.njk" import govukCheckboxes %}

{{ govukCheckboxes({
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
      "name": "british",
      "id": "item_british",
      "value": "yes",
      "text": "British"
    },
    {
      "name": "irish",
      "id": "item_irish",
      "value": "irish",
      "text": "Irish"
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

  <fieldset class="govuk-fieldset" aria-describedby="undefined-hint">

  <legend class="govuk-fieldset__legend">
    What is your nationality?
  </legend>

  <span id="undefined-hint" class="govuk-hint">
    If you have dual nationality, select all options that are relevant to you.
  </span>

  <div class="govuk-checkboxes">

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="item_british" name="british" type="checkbox" value="yes">
      <label class="govuk-label govuk-checkboxes__label" for="item_british">
        British
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="item_irish" name="irish" type="checkbox" value="irish">
      <label class="govuk-label govuk-checkboxes__label" for="item_irish">
        Irish
      </label>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )


def test_checkboxes_with_hints_on_items(env):
    template = env.from_string(
"""
{% from "checkboxes/macro.njk" import govukCheckboxes %}

{{ govukCheckboxes({
  "fieldset": {
    "legend": {
      "text": "How do you want to sign in?",
      "isPageHeading": true
    }
  },
  "items": [
    {
      "name": "gateway",
      "id": "government-gateway",
      "value": "gov-gateway",
      "text": "Sign in with Government Gateway",
      "hint": {
        "text": "You’ll have a user ID if you’ve registered for Self Assessment or filed a tax return online before."
      }
    },
    {
      "name": "verify",
      "id": "govuk-verify",
      "value": "gov-verify",
      "text": "Sign in with GOV.UK Verify",
      "hint": {
        "text": "You’ll have an account if you’ve already proved your identity with either Barclays, CitizenSafe, Digidentity, Experian, Post Office, Royal Mail or SecureIdentity."
      }
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

  <fieldset class="govuk-fieldset">

  <legend class="govuk-fieldset__legend">
    <h1 class="govuk-fieldset__heading">
      How do you want to sign in?
    </h1>
  </legend>

  <div class="govuk-checkboxes">

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="government-gateway" name="gateway" type="checkbox" value="gov-gateway" aria-describedby="government-gateway-item-hint">
      <label class="govuk-label govuk-checkboxes__label" for="government-gateway">
        Sign in with Government Gateway
      </label>
      <span id="government-gateway-item-hint" class="govuk-hint govuk-checkboxes__hint">
        You’ll have a user ID if you’ve registered for Self Assessment or filed a tax return online before.
      </span>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="govuk-verify" name="verify" type="checkbox" value="gov-verify" aria-describedby="govuk-verify-item-hint">
      <label class="govuk-label govuk-checkboxes__label" for="govuk-verify">
        Sign in with GOV.UK Verify
      </label>
      <span id="govuk-verify-item-hint" class="govuk-hint govuk-checkboxes__hint">
        You’ll have an account if you’ve already proved your identity with either Barclays, CitizenSafe, Digidentity, Experian, Post Office, Royal Mail or SecureIdentity.
      </span>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )


def test_checkboxes_with_disabled_item(env):
    template = env.from_string(
"""
{% from "checkboxes/macro.njk" import govukCheckboxes %}

{{ govukCheckboxes({
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
      "text": "Blue",
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

  <div class="govuk-checkboxes">

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="colours-1" name="colours" type="checkbox" value="red">
      <label class="govuk-label govuk-checkboxes__label" for="colours-1">
        Red
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="colours-2" name="colours" type="checkbox" value="green">
      <label class="govuk-label govuk-checkboxes__label" for="colours-2">
        Green
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="colours-3" name="colours" type="checkbox" value="blue" disabled>
      <label class="govuk-label govuk-checkboxes__label" for="colours-3">
        Blue
      </label>
    </div>

  </div>

</div>
"""
        )
    )


def test_checkboxes_with_legend_as_page_heading(env):
    template = env.from_string(
"""
{% from "checkboxes/macro.njk" import govukCheckboxes %}

{{ govukCheckboxes({
  "name": "waste",
  "fieldset": {
    "legend": {
      "text": "Which types of waste do you transport regularly?",
      "classes": "govuk-fieldset__legend--l",
      "isPageHeading": true
    }
  },
  "hint": {
    "text": "Select all that apply"
  },
  "items": [
    {
      "value": "animal",
      "text": "Waste from animal carcasses"
    },
    {
      "value": "mines",
      "text": "Waste from mines or quarries"
    },
    {
      "value": "farm",
      "text": "Farm or agricultural waste"
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

  <fieldset class="govuk-fieldset" aria-describedby="waste-hint">

  <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
    <h1 class="govuk-fieldset__heading">
      Which types of waste do you transport regularly?
    </h1>
  </legend>

  <span id="waste-hint" class="govuk-hint">
    Select all that apply
  </span>

  <div class="govuk-checkboxes">

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="waste-1" name="waste" type="checkbox" value="animal">
      <label class="govuk-label govuk-checkboxes__label" for="waste-1">
        Waste from animal carcasses
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="waste-2" name="waste" type="checkbox" value="mines">
      <label class="govuk-label govuk-checkboxes__label" for="waste-2">
        Waste from mines or quarries
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="waste-3" name="waste" type="checkbox" value="farm">
      <label class="govuk-label govuk-checkboxes__label" for="waste-3">
        Farm or agricultural waste
      </label>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )


def test_checkboxes_with_a_medium_legend(env):
    template = env.from_string(
"""
{% from "checkboxes/macro.njk" import govukCheckboxes %}

{{ govukCheckboxes({
  "name": "waste",
  "fieldset": {
    "legend": {
      "text": "Which types of waste do you transport regularly?",
      "classes": "govuk-fieldset__legend--m"
    }
  },
  "hint": {
    "text": "Select all that apply"
  },
  "errorMessage": {
    "text": "Select which types of waste you transport regularly"
  },
  "items": [
    {
      "value": "animal",
      "text": "Waste from animal carcasses"
    },
    {
      "value": "mines",
      "text": "Waste from mines or quarries"
    },
    {
      "value": "farm",
      "text": "Farm or agricultural waste"
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
<div class="govuk-form-group govuk-form-group--error">

  <fieldset class="govuk-fieldset" aria-describedby="waste-hint waste-error">

  <legend class="govuk-fieldset__legend govuk-fieldset__legend--m">
    Which types of waste do you transport regularly?
  </legend>

  <span id="waste-hint" class="govuk-hint">
    Select all that apply
  </span>

  <span id="waste-error" class="govuk-error-message">
    Select which types of waste you transport regularly
  </span>

  <div class="govuk-checkboxes">

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="waste-1" name="waste" type="checkbox" value="animal">
      <label class="govuk-label govuk-checkboxes__label" for="waste-1">
        Waste from animal carcasses
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="waste-2" name="waste" type="checkbox" value="mines">
      <label class="govuk-label govuk-checkboxes__label" for="waste-2">
        Waste from mines or quarries
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="waste-3" name="waste" type="checkbox" value="farm">
      <label class="govuk-label govuk-checkboxes__label" for="waste-3">
        Farm or agricultural waste
      </label>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )


def test_checkboxes_without_fieldset(env):
    template = env.from_string(
"""
{% from "checkboxes/macro.njk" import govukCheckboxes %}

{{ govukCheckboxes({
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

  <div class="govuk-checkboxes">

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="colours-1" name="colours" type="checkbox" value="red">
      <label class="govuk-label govuk-checkboxes__label" for="colours-1">
        Red
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="colours-2" name="colours" type="checkbox" value="green">
      <label class="govuk-label govuk-checkboxes__label" for="colours-2">
        Green
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="colours-3" name="colours" type="checkbox" value="blue">
      <label class="govuk-label govuk-checkboxes__label" for="colours-3">
        Blue
      </label>
    </div>

  </div>

</div>
"""
        )
    )


def test_checkboxes_with_all_fieldset_attributes(env):
    template = env.from_string(
"""
{% from "checkboxes/macro.njk" import govukCheckboxes %}

{{ govukCheckboxes({
  "idPrefix": "example",
  "name": "example",
  "fieldset": {
    "classes": "app-fieldset--custom-modifier",
    "attributes": {
      "data-attribute": "value",
      "data-second-attribute": "second-value"
    },
    "legend": {
      "text": "What is your nationality?"
    }
  },
  "hint": {
    "text": "If you have dual nationality, select all options that are relevant to you."
  },
  "errorMessage": {
    "text": "Please select an option"
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
<div class="govuk-form-group govuk-form-group--error">

  <fieldset class="govuk-fieldset app-fieldset--custom-modifier" aria-describedby="example-hint example-error" data-attribute="value" data-second-attribute="second-value">

  <legend class="govuk-fieldset__legend">
    What is your nationality?
  </legend>

  <span id="example-hint" class="govuk-hint">
    If you have dual nationality, select all options that are relevant to you.
  </span>

  <span id="example-error" class="govuk-error-message">
    Please select an option
  </span>

  <div class="govuk-checkboxes">

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="example-1" name="example" type="checkbox" value="british">
      <label class="govuk-label govuk-checkboxes__label" for="example-1">
        British
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="example-2" name="example" type="checkbox" value="irish">
      <label class="govuk-label govuk-checkboxes__label" for="example-2">
        Irish
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="example-3" name="example" type="checkbox" value="other">
      <label class="govuk-label govuk-checkboxes__label" for="example-3">
        Citizen of another country
      </label>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )


def test_checkboxes_with_error_message(env):
    template = env.from_string(
"""
{% from "checkboxes/macro.njk" import govukCheckboxes %}

{{ govukCheckboxes({
  "name": "waste",
  "errorMessage": {
    "text": "Please select an option"
  },
  "fieldset": {
    "legend": {
      "text": "Which types of waste do you transport regularly?"
    }
  },
  "items": [
    {
      "value": "animal",
      "text": "Waste from animal carcasses"
    },
    {
      "value": "mines",
      "text": "Waste from mines or quarries"
    },
    {
      "value": "farm",
      "text": "Farm or agricultural waste"
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
<div class="govuk-form-group govuk-form-group--error">

  <fieldset class="govuk-fieldset" aria-describedby="waste-error">

  <legend class="govuk-fieldset__legend">
    Which types of waste do you transport regularly?
  </legend>

  <span id="waste-error" class="govuk-error-message">
    Please select an option
  </span>

  <div class="govuk-checkboxes">

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="waste-1" name="waste" type="checkbox" value="animal">
      <label class="govuk-label govuk-checkboxes__label" for="waste-1">
        Waste from animal carcasses
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="waste-2" name="waste" type="checkbox" value="mines">
      <label class="govuk-label govuk-checkboxes__label" for="waste-2">
        Waste from mines or quarries
      </label>
    </div>

    <div class="govuk-checkboxes__item">
      <input class="govuk-checkboxes__input" id="waste-3" name="waste" type="checkbox" value="farm">
      <label class="govuk-label govuk-checkboxes__label" for="waste-3">
        Farm or agricultural waste
      </label>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )
