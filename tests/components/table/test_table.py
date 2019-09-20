
import pytest


def test_table(env):
    template = env.from_string(
"""
{% from "table/macro.njk" import govukTable %}

{{ govukTable({
  "rows": [
    [
      {
        "text": "January"
      },
      {
        "text": "£85",
        "format": "numeric"
      },
      {
        "text": "£95",
        "format": "numeric"
      }
    ],
    [
      {
        "text": "February"
      },
      {
        "text": "£75",
        "format": "numeric"
      },
      {
        "text": "£55",
        "format": "numeric"
      }
    ],
    [
      {
        "text": "March"
      },
      {
        "text": "£165",
        "format": "numeric"
      },
      {
        "text": "£125",
        "format": "numeric"
      }
    ]
  ]
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<table class="govuk-table">

  <tbody class="govuk-table__body">

    <tr class="govuk-table__row">

      <td class="govuk-table__cell">January</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£85</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£95</td>

    </tr>

    <tr class="govuk-table__row">

      <td class="govuk-table__cell">February</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£75</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£55</td>

    </tr>

    <tr class="govuk-table__row">

      <td class="govuk-table__cell">March</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£165</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£125</td>

    </tr>

  </tbody>
</table>
"""
        )
    )


def test_table_with_head(env):
    template = env.from_string(
"""
{% from "table/macro.njk" import govukTable %}

{{ govukTable({
  "head": [
    {
      "text": "Month you apply"
    },
    {
      "text": "Rate for bicycles",
      "format": "numeric"
    },
    {
      "text": "Rate for vehicles",
      "format": "numeric"
    }
  ],
  "rows": [
    [
      {
        "text": "January"
      },
      {
        "text": "£85",
        "format": "numeric"
      },
      {
        "text": "£95",
        "format": "numeric"
      }
    ],
    [
      {
        "text": "February"
      },
      {
        "text": "£75",
        "format": "numeric"
      },
      {
        "text": "£55",
        "format": "numeric"
      }
    ],
    [
      {
        "text": "March"
      },
      {
        "text": "£165",
        "format": "numeric"
      },
      {
        "text": "£125",
        "format": "numeric"
      }
    ]
  ]
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<table class="govuk-table">

  <thead class="govuk-table__head">
    <tr class="govuk-table__row">

      <th class="govuk-table__header" scope="col">Month you apply</th>

      <th class="govuk-table__header govuk-table__header--numeric" scope="col">Rate for bicycles</th>

      <th class="govuk-table__header govuk-table__header--numeric" scope="col">Rate for vehicles</th>

    </tr>
  </thead>

  <tbody class="govuk-table__body">

    <tr class="govuk-table__row">

      <td class="govuk-table__cell">January</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£85</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£95</td>

    </tr>

    <tr class="govuk-table__row">

      <td class="govuk-table__cell">February</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£75</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£55</td>

    </tr>

    <tr class="govuk-table__row">

      <td class="govuk-table__cell">March</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£165</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£125</td>

    </tr>

  </tbody>
</table>
"""
        )
    )


def test_table_with_head_and_caption(env):
    template = env.from_string(
"""
{% from "table/macro.njk" import govukTable %}

{{ govukTable({
  "caption": "Caption 1: Months and rates",
  "captionClasses": "govuk-heading-m",
  "firstCellIsHeader": true,
  "head": [
    {
      "text": "Month you apply"
    },
    {
      "text": "Rate for bicycles",
      "format": "numeric"
    },
    {
      "text": "Rate for vehicles",
      "format": "numeric"
    }
  ],
  "rows": [
    [
      {
        "text": "January"
      },
      {
        "text": "£85",
        "format": "numeric"
      },
      {
        "text": "£95",
        "format": "numeric"
      }
    ],
    [
      {
        "text": "February"
      },
      {
        "text": "£75",
        "format": "numeric"
      },
      {
        "text": "£55",
        "format": "numeric"
      }
    ],
    [
      {
        "text": "March"
      },
      {
        "text": "£165",
        "format": "numeric"
      },
      {
        "text": "£125",
        "format": "numeric"
      }
    ]
  ]
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<table class="govuk-table">

  <caption class="govuk-table__caption govuk-heading-m">Caption 1: Months and rates</caption>

  <thead class="govuk-table__head">
    <tr class="govuk-table__row">

      <th class="govuk-table__header" scope="col">Month you apply</th>

      <th class="govuk-table__header govuk-table__header--numeric" scope="col">Rate for bicycles</th>

      <th class="govuk-table__header govuk-table__header--numeric" scope="col">Rate for vehicles</th>

    </tr>
  </thead>

  <tbody class="govuk-table__body">

    <tr class="govuk-table__row">

      <th class="govuk-table__header" scope="row">January</th>

      <td class="govuk-table__cell govuk-table__cell--numeric">£85</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£95</td>

    </tr>

    <tr class="govuk-table__row">

      <th class="govuk-table__header" scope="row">February</th>

      <td class="govuk-table__cell govuk-table__cell--numeric">£75</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£55</td>

    </tr>

    <tr class="govuk-table__row">

      <th class="govuk-table__header" scope="row">March</th>

      <td class="govuk-table__cell govuk-table__cell--numeric">£165</td>

      <td class="govuk-table__cell govuk-table__cell--numeric">£125</td>

    </tr>

  </tbody>
</table>
"""
        )
    )
