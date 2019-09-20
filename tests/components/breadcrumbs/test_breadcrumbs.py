
import pytest


def test_breadcrumbs(env):
    template = env.from_string(
"""
{% from "breadcrumbs/macro.njk" import govukBreadcrumbs %}

{{ govukBreadcrumbs({
  "items": [
    {
      "text": "Section",
      "href": "/section"
    },
    {
      "text": "Sub-section",
      "href": "/section/sub-section"
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
<div class="govuk-breadcrumbs">
  <ol class="govuk-breadcrumbs__list">

    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="/section">Section</a>
    </li>

    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="/section/sub-section">Sub-section</a>
    </li>

  </ol>
</div>
"""
        )
    )


def test_breadcrumbs_with_one_level(env):
    template = env.from_string(
"""
{% from "breadcrumbs/macro.njk" import govukBreadcrumbs %}

{{ govukBreadcrumbs({
  "items": [
    {
      "text": "Section",
      "href": "/section"
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
<div class="govuk-breadcrumbs">
  <ol class="govuk-breadcrumbs__list">

    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="/section">Section</a>
    </li>

  </ol>
</div>
"""
        )
    )


def test_breadcrumbs_with_multiple_levels(env):
    template = env.from_string(
"""
{% from "breadcrumbs/macro.njk" import govukBreadcrumbs %}

{{ govukBreadcrumbs({
  "items": [
    {
      "text": "Home",
      "href": "/"
    },
    {
      "text": "Section",
      "href": "/section"
    },
    {
      "text": "Sub-section",
      "href": "/section/sub-section"
    },
    {
      "text": "Sub Sub-section",
      "href": "/section/sub-section/sub-sub-section"
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
<div class="govuk-breadcrumbs">
  <ol class="govuk-breadcrumbs__list">

    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="/">Home</a>
    </li>

    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="/section">Section</a>
    </li>

    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="/section/sub-section">Sub-section</a>
    </li>

    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="/section/sub-section/sub-sub-section">Sub Sub-section</a>
    </li>

  </ol>
</div>
"""
        )
    )


def test_breadcrumbs_without_the_home_section(env):
    template = env.from_string(
"""
{% from "breadcrumbs/macro.njk" import govukBreadcrumbs %}

{{ govukBreadcrumbs({
  "items": [
    {
      "text": "Service Manual",
      "href": "/service-manual"
    },
    {
      "text": "Agile Delivery",
      "href": "/service-manual/agile-delivery"
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
<div class="govuk-breadcrumbs">
  <ol class="govuk-breadcrumbs__list">

    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="/service-manual">Service Manual</a>
    </li>

    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="/service-manual/agile-delivery">Agile Delivery</a>
    </li>

  </ol>
</div>
"""
        )
    )


def test_breadcrumbs_with_last_breadcrumb_as_current_page(env):
    template = env.from_string(
"""
{% from "breadcrumbs/macro.njk" import govukBreadcrumbs %}

{{ govukBreadcrumbs({
  "items": [
    {
      "text": "Home",
      "href": "/"
    },
    {
      "text": "Passports, travel and living abroad",
      "href": "/browse/abroad"
    },
    {
      "text": "Travel abroad"
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
<div class="govuk-breadcrumbs">
  <ol class="govuk-breadcrumbs__list">

    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="/">Home</a>
    </li>

    <li class="govuk-breadcrumbs__list-item">
      <a class="govuk-breadcrumbs__link" href="/browse/abroad">Passports, travel and living abroad</a>
    </li>

    <li class="govuk-breadcrumbs__list-item" aria-current="page">Travel abroad</li>

  </ol>
</div>
"""
        )
    )
