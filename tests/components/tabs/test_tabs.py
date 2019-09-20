
import pytest


def test_tabs(env):
    template = env.from_string(
r"""
{% from "tabs/macro.njk" import govukTabs %}

{{ govukTabs({
  "items": [
    {
      "label": "Past day",
      "id": "past-day",
      "panel": {
        "html": "<h2 class=\"govuk-heading-l\">Past day</h2>\n<table class=\"govuk-table\">\n  <thead class=\"govuk-table__head\">\n    <tr class=\"govuk-table__row\">\n      <th class=\"govuk-table__header\" scope=\"col\">Case manager</th>\n      <th class=\"govuk-table__header\" scope=\"col\">Cases opened</th>\n      <th class=\"govuk-table__header\" scope=\"col\">Cases closed</th>\n    </tr>\n  </thead>\n  <tbody class=\"govuk-table__body\">\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">David Francis</td>\n      <td class=\"govuk-table__cell\">3</td>\n      <td class=\"govuk-table__cell\">0</td>\n    </tr>\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">Paul Farmer</td>\n      <td class=\"govuk-table__cell\">1</td>\n      <td class=\"govuk-table__cell\">0</td>\n    </tr>\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">Rita Patel</td>\n      <td class=\"govuk-table__cell\">2</td>\n      <td class=\"govuk-table__cell\">0</td>\n    </tr>\n  </tbody>\n</table>\n"
      }
    },
    {
      "label": "Past week",
      "id": "past-week",
      "panel": {
        "html": "<h2 class=\"govuk-heading-l\">Past week</h2>\n<table class=\"govuk-table\">\n  <thead class=\"govuk-table__head\">\n    <tr class=\"govuk-table__row\">\n      <th class=\"govuk-table__header\" scope=\"col\">Case manager</th>\n      <th class=\"govuk-table__header\" scope=\"col\">Cases opened</th>\n      <th class=\"govuk-table__header\" scope=\"col\">Cases closed</th>\n    </tr>\n  </thead>\n  <tbody class=\"govuk-table__body\">\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">David Francis</td>\n      <td class=\"govuk-table__cell\">24</td>\n      <td class=\"govuk-table__cell\">18</td>\n    </tr>\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">Paul Farmer</td>\n      <td class=\"govuk-table__cell\">16</td>\n      <td class=\"govuk-table__cell\">20</td>\n    </tr>\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">Rita Patel</td>\n      <td class=\"govuk-table__cell\">24</td>\n      <td class=\"govuk-table__cell\">27</td>\n    </tr>\n  </tbody>\n</table>\n"
      }
    },
    {
      "label": "Past month",
      "id": "past-month",
      "panel": {
        "html": "<h2 class=\"govuk-heading-l\">Past month</h2>\n<table class=\"govuk-table\">\n  <thead class=\"govuk-table__head\">\n    <tr class=\"govuk-table__row\">\n      <th class=\"govuk-table__header\" scope=\"col\">Case manager</th>\n      <th class=\"govuk-table__header\" scope=\"col\">Cases opened</th>\n      <th class=\"govuk-table__header\" scope=\"col\">Cases closed</th>\n    </tr>\n  </thead>\n  <tbody class=\"govuk-table__body\">\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">David Francis</td>\n      <td class=\"govuk-table__cell\">98</td>\n      <td class=\"govuk-table__cell\">95</td>\n    </tr>\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">Paul Farmer</td>\n      <td class=\"govuk-table__cell\">122</td>\n      <td class=\"govuk-table__cell\">131</td>\n    </tr>\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">Rita Patel</td>\n      <td class=\"govuk-table__cell\">126</td>\n      <td class=\"govuk-table__cell\">142</td>\n    </tr>\n  </tbody>\n</table>\n"
      }
    },
    {
      "label": "Past year",
      "id": "past-year",
      "panel": {
        "html": "<h2 class=\"govuk-heading-l\">Past year</h2>\n<table class=\"govuk-table\">\n  <thead class=\"govuk-table__head\">\n    <tr class=\"govuk-table__row\">\n      <th class=\"govuk-table__header\" scope=\"col\">Case manager</th>\n      <th class=\"govuk-table__header\" scope=\"col\">Cases opened</th>\n      <th class=\"govuk-table__header\" scope=\"col\">Cases closed</th>\n    </tr>\n  </thead>\n  <tbody class=\"govuk-table__body\">\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">David Francis</td>\n      <td class=\"govuk-table__cell\">1380</td>\n      <td class=\"govuk-table__cell\">1472</td>\n    </tr>\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">Paul Farmer</td>\n      <td class=\"govuk-table__cell\">1129</td>\n      <td class=\"govuk-table__cell\">1083</td>\n    </tr>\n    <tr class=\"govuk-table__row\">\n      <td class=\"govuk-table__cell\">Rita Patel</td>\n      <td class=\"govuk-table__cell\">1539</td>\n      <td class=\"govuk-table__cell\">1265</td>\n    </tr>\n  </tbody>\n</table>\n"
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
<div class="govuk-tabs" data-module="tabs">
  <h2 class="govuk-tabs__title">
    Contents
  </h2>

  <ul class="govuk-tabs__list">

      <li class="govuk-tabs__list-item">
        <a class="govuk-tabs__tab govuk-tabs__tab--selected" href="#past-day">
          Past day
        </a>
      </li>

      <li class="govuk-tabs__list-item">
        <a class="govuk-tabs__tab" href="#past-week">
          Past week
        </a>
      </li>

      <li class="govuk-tabs__list-item">
        <a class="govuk-tabs__tab" href="#past-month">
          Past month
        </a>
      </li>

      <li class="govuk-tabs__list-item">
        <a class="govuk-tabs__tab" href="#past-year">
          Past year
        </a>
      </li>

  </ul>

  <section class="govuk-tabs__panel" id="past-day">
    <h2 class="govuk-heading-l">Past day</h2>
<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th class="govuk-table__header" scope="col">Case manager</th>
      <th class="govuk-table__header" scope="col">Cases opened</th>
      <th class="govuk-table__header" scope="col">Cases closed</th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">David Francis</td>
      <td class="govuk-table__cell">3</td>
      <td class="govuk-table__cell">0</td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">Paul Farmer</td>
      <td class="govuk-table__cell">1</td>
      <td class="govuk-table__cell">0</td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">Rita Patel</td>
      <td class="govuk-table__cell">2</td>
      <td class="govuk-table__cell">0</td>
    </tr>
  </tbody>
</table>

  </section>

  <section class="govuk-tabs__panel govuk-tabs__panel--hidden" id="past-week">
    <h2 class="govuk-heading-l">Past week</h2>
<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th class="govuk-table__header" scope="col">Case manager</th>
      <th class="govuk-table__header" scope="col">Cases opened</th>
      <th class="govuk-table__header" scope="col">Cases closed</th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">David Francis</td>
      <td class="govuk-table__cell">24</td>
      <td class="govuk-table__cell">18</td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">Paul Farmer</td>
      <td class="govuk-table__cell">16</td>
      <td class="govuk-table__cell">20</td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">Rita Patel</td>
      <td class="govuk-table__cell">24</td>
      <td class="govuk-table__cell">27</td>
    </tr>
  </tbody>
</table>

  </section>

  <section class="govuk-tabs__panel govuk-tabs__panel--hidden" id="past-month">
    <h2 class="govuk-heading-l">Past month</h2>
<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th class="govuk-table__header" scope="col">Case manager</th>
      <th class="govuk-table__header" scope="col">Cases opened</th>
      <th class="govuk-table__header" scope="col">Cases closed</th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">David Francis</td>
      <td class="govuk-table__cell">98</td>
      <td class="govuk-table__cell">95</td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">Paul Farmer</td>
      <td class="govuk-table__cell">122</td>
      <td class="govuk-table__cell">131</td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">Rita Patel</td>
      <td class="govuk-table__cell">126</td>
      <td class="govuk-table__cell">142</td>
    </tr>
  </tbody>
</table>

  </section>

  <section class="govuk-tabs__panel govuk-tabs__panel--hidden" id="past-year">
    <h2 class="govuk-heading-l">Past year</h2>
<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th class="govuk-table__header" scope="col">Case manager</th>
      <th class="govuk-table__header" scope="col">Cases opened</th>
      <th class="govuk-table__header" scope="col">Cases closed</th>
    </tr>
  </thead>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">David Francis</td>
      <td class="govuk-table__cell">1380</td>
      <td class="govuk-table__cell">1472</td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">Paul Farmer</td>
      <td class="govuk-table__cell">1129</td>
      <td class="govuk-table__cell">1083</td>
    </tr>
    <tr class="govuk-table__row">
      <td class="govuk-table__cell">Rita Patel</td>
      <td class="govuk-table__cell">1539</td>
      <td class="govuk-table__cell">1265</td>
    </tr>
  </tbody>
</table>

  </section>

</div>
"""
        )
    )


def test_tabs_simple(env):
    template = env.from_string(
"""
{% from "tabs/macro.njk" import govukTabs %}

{{ govukTabs({
  "items": [
    {
      "label": "Past day",
      "id": "past-day",
      "panel": {
        "text": "Yesterday"
      }
    },
    {
      "label": "This day",
      "id": "this-day",
      "panel": {
        "text": "Today"
      }
    },
    {
      "label": "Next day",
      "id": "next-day",
      "panel": {
        "text": "Tomorrow"
      }
    },
  ]
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-tabs" data-module="tabs">
  <h2 class="govuk-tabs__title">
    Contents
  </h2>

  <ul class="govuk-tabs__list">

      <li class="govuk-tabs__list-item">
        <a class="govuk-tabs__tab govuk-tabs__tab--selected" href="#past-day">
          Past day
        </a>
      </li>

      <li class="govuk-tabs__list-item">
        <a class="govuk-tabs__tab" href="#this-day">
          This day
        </a>
      </li>

      <li class="govuk-tabs__list-item">
        <a class="govuk-tabs__tab" href="#next-day">
          Next day
        </a>
      </li>

  </ul>

  <section class="govuk-tabs__panel" id="past-day">
    Yesterday
  </section>

  <section class="govuk-tabs__panel govuk-tabs__panel--hidden" id="this-day">
    Today
  </section>

  <section class="govuk-tabs__panel govuk-tabs__panel--hidden" id="next-day">
    Tomorrow
  </section>
</div>
"""
        )
    )
