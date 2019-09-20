
import pytest

from govuk_frontend_jinja.templates import njk_to_j2


def test_replaces_items_getattr_with_getitem():
    assert (
        njk_to_j2 (
"""
{% for item in params.items %}
  item
{% endfor %}
"""
        )
        ==
"""
{% for item in params['items'] %}
  item
{% endfor %}
"""
    )


def test_replaces_add_loop_index_with_concatenate():
    assert (
        njk_to_j2(
"""
{% for item in items %}
  "item " + loop.index
{% endfor %}
"""
        )
        ==
"""
{% for item in items %}
  "item " ~ loop.index
{% endfor %}
"""
    )


def test_quotes_dictionary_keys():
    assert (
        njk_to_j2(
"""
{{ macro({
  param: 'foo',
  value: 'bar'
}) }}
"""
        )
        ==
"""
{{ macro({
  'param': 'foo',
  'value': 'bar'
}) }}
"""
    )


def test_patches_govuk_fieldset_definition():
    assert(
        njk_to_j2("{% macro govukFieldset(params) %}{% endmacro %}")
        ==
        "{% macro govukFieldset(params, caller=none) %}{% endmacro %}"
    )


def test_patches_iteration_of_params_attributes():
    assert (
        njk_to_j2("{%- for attribute, value in params.attributes %}{% endfor -%}")
        ==
        "{%- for attribute, value in params.attributes.items() %}{% endfor -%}"
    )


def test_adds_nonlocal_namespace_if_template_includes_describedBy():
    template = """
    {% set describedBy = "" %}
    """
    assert "    {%- set nonlocal = namespace() -%}" in njk_to_j2(template)


def test_patches_describedBy_to_set_nonlocal():
    template = \
"""
{% set describedBy = "" %}
{% set describedBy = describedBy + '-hint' %}
{% if ((describedBy | length) > 0) %}{% endif %}
{% macro x(params) %}
  {{ params.describedBy }}
{% endmacro %}
x({
    "describedBy": describedBy,
    describedBy: describedBy,
})
"""
    assert (
        njk_to_j2(template)
        ==
"""
{%- set nonlocal = namespace() -%}
{% set nonlocal.describedBy = "" %}
{% set nonlocal.describedBy = nonlocal.describedBy + '-hint' %}
{% if ((nonlocal.describedBy | length) > 0) %}{% endif %}
{% macro x(params) %}
  {{ params.describedBy }}
{% endmacro %}
x({
    "describedBy": nonlocal.describedBy,
    'describedBy': nonlocal.describedBy,
})
"""
    )


def test_replaces_length_getattr_with_length_filter():
    assert (
        njk_to_j2("{{ params.length }}")
        ==
        "{{ params | length }}"
    )
