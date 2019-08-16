
import pytest

from govuk_frontend.templates import Environment


def test_radios(env):
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


def test_radios_without_fieldset(env):
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


def test_radios_with_disabled(env):
    template = env.from_string(
"""
{% from "radios/macro.njk" import govukRadios %}

{{ govukRadios({
  "idPrefix": "example-disabled",
  "name": "example-disabled",
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
      "text": "Yes",
      "disabled": true
    },
    {
      "value": "no",
      "text": "No",
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

  <fieldset class="govuk-fieldset" aria-describedby="example-disabled-hint">

  <legend class="govuk-fieldset__legend">
    Have you changed your name?
  </legend>

  <span id="example-disabled-hint" class="govuk-hint">
    This includes changing your last name or spelling your name differently.
  </span>

  <div class="govuk-radios">

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="example-disabled-1" name="example-disabled" type="radio" value="yes" disabled>
      <label class="govuk-label govuk-radios__label" for="example-disabled-1">
        Yes
      </label>
    </div>

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="example-disabled-2" name="example-disabled" type="radio" value="no" disabled>
      <label class="govuk-label govuk-radios__label" for="example-disabled-2">
        No
      </label>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )


def test_radios_with_legend_as_page_heading(env):
    template = env.from_string(
r"""
{% from "radios/macro.njk" import govukRadios %}

{{ govukRadios({
  "idPrefix": "housing-act",
  "name": "housing-act",
  "fieldset": {
    "legend": {
      "text": "Which part of the Housing Act was your licence issued under?",
      "classes": "govuk-fieldset__legend--l",
      "isPageHeading": true
    }
  },
  "hint": {
    "text": "Select one of the options below."
  },
  "items": [
    {
      "value": "part-2",
      "html": "<span class=\"govuk-heading-s govuk-!-margin-bottom-1\">Part 2 of the Housing Act 2004</span> For properties that are 3 or more stories high and occupied by 5 or more people"
    },
    {
      "value": "part-3",
      "html": "<span class=\"govuk-heading-s govuk-!-margin-bottom-1\">Part 3 of the Housing Act 2004</span> For properties that are within a geographical area defined by a local council"
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

  <fieldset class="govuk-fieldset" aria-describedby="housing-act-hint">

  <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
    <h1 class="govuk-fieldset__heading">
      Which part of the Housing Act was your licence issued under?
    </h1>
  </legend>

  <span id="housing-act-hint" class="govuk-hint">
    Select one of the options below.
  </span>

  <div class="govuk-radios">

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="housing-act-1" name="housing-act" type="radio" value="part-2">
      <label class="govuk-label govuk-radios__label" for="housing-act-1">
        <span class="govuk-heading-s govuk-!-margin-bottom-1">Part 2 of the Housing Act 2004</span> For properties that are 3 or more stories high and occupied by 5 or more people
      </label>
    </div>

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="housing-act-2" name="housing-act" type="radio" value="part-3">
      <label class="govuk-label govuk-radios__label" for="housing-act-2">
        <span class="govuk-heading-s govuk-!-margin-bottom-1">Part 3 of the Housing Act 2004</span> For properties that are within a geographical area defined by a local council
      </label>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )


def test_radios_with_a_medium_legend(env):
    template = env.from_string(
r"""
{% from "radios/macro.njk" import govukRadios %}

{{ govukRadios({
  "idPrefix": "housing-act",
  "name": "housing-act",
  "fieldset": {
    "legend": {
      "text": "Which part of the Housing Act was your licence issued under?",
      "classes": "govuk-fieldset__legend--m"
    }
  },
  "hint": {
    "text": "Select one of the options below."
  },
  "items": [
    {
      "value": "part-2",
      "html": "<span class=\"govuk-heading-s govuk-!-margin-bottom-1\">Part 2 of the Housing Act 2004</span> For properties that are 3 or more stories high and occupied by 5 or more people"
    },
    {
      "value": "part-3",
      "html": "<span class=\"govuk-heading-s govuk-!-margin-bottom-1\">Part 3 of the Housing Act 2004</span> For properties that are within a geographical area defined by a local council"
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

  <fieldset class="govuk-fieldset" aria-describedby="housing-act-hint">

  <legend class="govuk-fieldset__legend govuk-fieldset__legend--m">
    Which part of the Housing Act was your licence issued under?
  </legend>

  <span id="housing-act-hint" class="govuk-hint">
    Select one of the options below.
  </span>

  <div class="govuk-radios">

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="housing-act-1" name="housing-act" type="radio" value="part-2">
      <label class="govuk-label govuk-radios__label" for="housing-act-1">
        <span class="govuk-heading-s govuk-!-margin-bottom-1">Part 2 of the Housing Act 2004</span> For properties that are 3 or more stories high and occupied by 5 or more people
      </label>
    </div>

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="housing-act-2" name="housing-act" type="radio" value="part-3">
      <label class="govuk-label govuk-radios__label" for="housing-act-2">
        <span class="govuk-heading-s govuk-!-margin-bottom-1">Part 3 of the Housing Act 2004</span> For properties that are within a geographical area defined by a local council
      </label>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )


def test_radios_with_a_divider(env):
    template = env.from_string(
"""
{% from "radios/macro.njk" import govukRadios %}

{{ govukRadios({
  "idPrefix": "example-divider",
  "name": "example",
  "fieldset": {
    "legend": {
      "text": "How do you want to sign in?"
    }
  },
  "items": [
    {
      "value": "governement-gateway",
      "text": "Use Government Gateway"
    },
    {
      "value": "govuk-verify",
      "text": "Use GOV.UK Verify"
    },
    {
      "divider": "or"
    },
    {
      "value": "create-account",
      "text": "Create an account"
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
    How do you want to sign in?
  </legend>

  <div class="govuk-radios">

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="example-divider-1" name="example" type="radio" value="governement-gateway">
      <label class="govuk-label govuk-radios__label" for="example-divider-1">
        Use Government Gateway
      </label>
    </div>

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="example-divider-2" name="example" type="radio" value="govuk-verify">
      <label class="govuk-label govuk-radios__label" for="example-divider-2">
        Use GOV.UK Verify
      </label>
    </div>

    <div class="govuk-radios__divider">or</div>

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="example-divider-4" name="example" type="radio" value="create-account">
      <label class="govuk-label govuk-radios__label" for="example-divider-4">
        Create an account
      </label>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )


@pytest.mark.xfail(reason="apostrophe not escaped")
def test_radios_with_hints_on_items(env):
    template = env.from_string(
"""
{% from "radios/macro.njk" import govukRadios %}

{{ govukRadios({
  "idPrefix": "gov",
  "name": "gov",
  "fieldset": {
    "legend": {
      "text": "How do you want to sign in?",
      "isPageHeading": true
    }
  },
  "items": [
    {
      "value": "gateway",
      "text": "Sign in with Government Gateway",
      "hint": {
        "text": "You'll have a user ID if you've registered for Self Assessment or filed a tax return online before."
      }
    },
    {
      "value": "verify",
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

  <div class="govuk-radios">

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="gov-1" name="gov" type="radio" value="gateway" aria-describedby="gov-1-item-hint">
      <label class="govuk-label govuk-radios__label" for="gov-1">
        Sign in with Government Gateway
      </label>
      <span id="gov-1-item-hint" class="govuk-hint govuk-radios__hint">
        You&#39;ll have a user ID if you&#39;ve registered for Self Assessment or filed a tax return online before.
      </span>
    </div>

    <div class="govuk-radios__item">
      <input class="govuk-radios__input" id="gov-2" name="gov" type="radio" value="verify" aria-describedby="gov-2-item-hint">
      <label class="govuk-label govuk-radios__label" for="gov-2">
        Sign in with GOV.UK Verify
      </label>
      <span id="gov-2-item-hint" class="govuk-hint govuk-radios__hint">
        You’ll have an account if you’ve already proved your identity with either Barclays, CitizenSafe, Digidentity, Experian, Post Office, Royal Mail or SecureIdentity.
      </span>
    </div>

  </div>
  </fieldset>

</div>
"""
        )
    )


def test_radios_without_fieldset(env):
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
        )
    )


def test_radios_with_all_fieldset_attributes(env):
    template = env.from_string(
"""
{% from "radios/macro.njk" import govukRadios %}

{{ govukRadios({
  "idPrefix": "example",
  "name": "example",
  "errorMessage": {
    "text": "Please select an option"
  },
  "fieldset": {
    "classes": "app-fieldset--custom-modifier",
    "attributes": {
      "data-attribute": "value",
      "data-second-attribute": "second-value"
    },
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
<div class="govuk-form-group govuk-form-group--error">

  <fieldset class="govuk-fieldset app-fieldset--custom-modifier" aria-describedby="example-hint example-error" data-attribute="value" data-second-attribute="second-value">

  <legend class="govuk-fieldset__legend">
    Have you changed your name?
  </legend>

  <span id="example-hint" class="govuk-hint">
    This includes changing your last name or spelling your name differently.
  </span>

  <span id="example-error" class="govuk-error-message">
    Please select an option
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
