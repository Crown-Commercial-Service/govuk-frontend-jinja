
import pytest

pytestmark = pytest.mark.skipif(
    pytest.helpers.govuk_frontend_version_info() < (2, 5),
    reason="requires govuk-frontend >= 2.5"
)


@pytest.mark.xfail(reason="differences in indentation")
def test_summary_list(env):
    template = env.from_string(
"""
{% from "components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  'rows': [
    {
      'key': {
        'text': "Name"
      },
      'value': {
        'text': "Sarah Philips"
      },
      'actions': {
        'items': [
          {
            'href': "#",
            'text': "Change",
            'visuallyHiddenText': "name"
          }
        ]
      }
    },
    {
      'key': {
        'text': "Date of birth"
      },
      'value': {
        'text': "5 January 1978"
      },
      'actions': {
        'items': [
          {
            'href': "#",
            'text': "Change",
            'visuallyHiddenText': "date of birth"
          }
        ]
      }
    },
    {
      'key': {
        'text': "Contact information"
      },
      'value': {
        'html': "72 Guild Street<br>London<br>SE23 6FH"
      },
      'actions': {
        'items': [
          {
            'href': "#",
            'text': "Change",
            'visuallyHiddenText': "contact information"
          }
        ]
      }
    },
    {
      'key': {
        'text': "Contact details"
      },
      'value': {
        'html': '<p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>'
      },
      'actions': {
        'items': [
          {
            'href': "#",
            'text': "Change",
            'visuallyHiddenText': "contact details"
          }
        ]
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
<dl class="govuk-summary-list">
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Name
      </dt>
      <dd class="govuk-summary-list__value">
        Sarah Philips
      </dd>
        <dd class="govuk-summary-list__actions">
            <a class="govuk-link" href="#">
                Change<span class="govuk-visually-hidden"> name</span>
            </a>
        </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Date of birth
      </dt>
      <dd class="govuk-summary-list__value">
        5 January 1978
      </dd>
        <dd class="govuk-summary-list__actions">
            <a class="govuk-link" href="#">
                Change<span class="govuk-visually-hidden"> date of birth</span>
            </a>
        </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Contact information
      </dt>
      <dd class="govuk-summary-list__value">
        72 Guild Street<br>London<br>SE23 6FH
      </dd>
        <dd class="govuk-summary-list__actions">
            <a class="govuk-link" href="#">
                Change<span class="govuk-visually-hidden"> contact information</span>
            </a>
        </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Contact details
      </dt>
      <dd class="govuk-summary-list__value">
        <p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>
      </dd>
        <dd class="govuk-summary-list__actions">
            <a class="govuk-link" href="#">
                Change<span class="govuk-visually-hidden"> contact details</span>
            </a>
        </dd>
    </div>
</dl>
"""
        )
    )


@pytest.mark.xfail(reason="differences in indentation")
def test_summary_list_with_actions(env):
    template = env.from_string(
"""
{% from "components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  'rows': [
    {
      'key': {
        'text': "Name"
      },
      'value': {
        'text': "Sarah Philips"
      },
      'actions': {
        'items': [
          {
            'href': "#",
            'text': "Change",
            'visuallyHiddenText': "name"
          }
        ]
      }
    },
    {
      'key': {
        'text': "Date of birth"
      },
      'value': {
        'text': "5 January 1978"
      },
      'actions': {
        'items': [
          {
            'href': "#",
            'text': "Change",
            'visuallyHiddenText': "date of birth"
          }
        ]
      }
    },
    {
      'key': {
        'text': "Contact information"
      },
      'value': {
        'html': "72 Guild Street<br>London<br>SE23 6FH"
      },
      'actions': {
        'items': [
          {
            'href': "#",
            'text': "Change",
            'visuallyHiddenText': "contact information"
          }
        ]
      }
    },
    {
      'key': {
        'text': "Contact details"
      },
      'value': {
        'html': '<p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>'
      },
      'actions': {
        'items': [
          {
            'href': "#",
            'text': "Change",
            'visuallyHiddenText': "contact details"
          }
        ]
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
<dl class="govuk-summary-list">
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Name
      </dt>
      <dd class="govuk-summary-list__value">
        Sarah Philips
      </dd>
        <dd class="govuk-summary-list__actions">
            <a class="govuk-link" href="#">
                Change<span class="govuk-visually-hidden"> name</span>
            </a>
        </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Date of birth
      </dt>
      <dd class="govuk-summary-list__value">
        5 January 1978
      </dd>
        <dd class="govuk-summary-list__actions">
            <a class="govuk-link" href="#">
                Change<span class="govuk-visually-hidden"> date of birth</span>
            </a>
        </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Contact information
      </dt>
      <dd class="govuk-summary-list__value">
        72 Guild Street<br>London<br>SE23 6FH
      </dd>
        <dd class="govuk-summary-list__actions">
            <a class="govuk-link" href="#">
                Change<span class="govuk-visually-hidden"> contact information</span>
            </a>
        </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Contact details
      </dt>
      <dd class="govuk-summary-list__value">
        <p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>
      </dd>
        <dd class="govuk-summary-list__actions">
            <a class="govuk-link" href="#">
                Change<span class="govuk-visually-hidden"> contact details</span>
            </a>
        </dd>
    </div>
</dl>
"""
        )
    )


def test_summary_link_without_actions(env):
    template = env.from_string(
"""
{% from "components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  'rows': [
    {
      'key': {
        'text': "Name"
      },
      'value': {
        'text': "Sarah Philips"
      }
    },
    {
      'key': {
        'text': "Date of birth"
      },
      'value': {
        'text': "5 January 1978"
      }
    },
    {
      'key': {
        'text': "Contact information"
      },
      'value': {
        'html': "72 Guild Street<br>London<br>SE23 6FH"
      }
    },
    {
      'key': {
        'text': "Contact details"
      },
      'value': {
        'html': '<p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>'
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
<dl class="govuk-summary-list">
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Name
      </dt>
      <dd class="govuk-summary-list__value">
        Sarah Philips
      </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Date of birth
      </dt>
      <dd class="govuk-summary-list__value">
        5 January 1978
      </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Contact information
      </dt>
      <dd class="govuk-summary-list__value">
        72 Guild Street<br>London<br>SE23 6FH
      </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Contact details
      </dt>
      <dd class="govuk-summary-list__value">
        <p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>
      </dd>
    </div>
</dl>
"""
        )
    )


def test_summary_link_without_borders(env):
    template = env.from_string(
"""
{% from "components/summary-list/macro.njk" import govukSummaryList %}

{{ govukSummaryList({
  'rows': [
    {
      'key': {
        'text': "Name"
      },
      'value': {
        'text': "Sarah Philips"
      }
    },
    {
      'key': {
        'text': "Date of birth"
      },
      'value': {
        'text': "5 January 1978"
      }
    },
    {
      'key': {
        'text': "Contact information"
      },
      'value': {
        'html': "72 Guild Street<br>London<br>SE23 6FH"
      }
    },
    {
      'key': {
        'text': "Contact details"
      },
      'value': {
        'html': '<p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>'
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
<dl class="govuk-summary-list">
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Name
      </dt>
      <dd class="govuk-summary-list__value">
        Sarah Philips
      </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Date of birth
      </dt>
      <dd class="govuk-summary-list__value">
        5 January 1978
      </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Contact information
      </dt>
      <dd class="govuk-summary-list__value">
        72 Guild Street<br>London<br>SE23 6FH
      </dd>
    </div>
    <div class="govuk-summary-list__row">
      <dt class="govuk-summary-list__key">
        Contact details
      </dt>
      <dd class="govuk-summary-list__value">
        <p class="govuk-body">07700 900457</p><p class="govuk-body">sarah.phillips@example.com</p>
      </dd>
    </div>
</dl>
"""
        )
    )
