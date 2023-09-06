
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
{% for item in params.items__njk %}
  item
{% endfor %}
"""
    )


def test_replaces_values_getattr_with_getitem():
    assert (
        njk_to_j2 (
"""
{% for value in params.values %}
  value
{% endfor %}
"""
        )
        ==
"""
{% for value in params.values__njk %}
  value
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

def test_replaces_add_max_words_with_concatenate():
    assert (
        njk_to_j2(
"""
{{ macro({
  text: 'You can enter up to ' + (params.maxlength or params.maxwords) + (' words' if params.maxwords else ' characters')
}) }}
"""
        )
        ==
"""
{{ macro({
  'text': 'You can enter up to ' ~ (params.maxlength or params.maxwords) ~ (' words' if params.maxwords else ' characters')
}) }}
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


@pytest.mark.parametrize("object", (
    "params",
    "item",
    "cell",
    "action"
))
def test_patches_iteration_of_attributes(object):
    assert (
        njk_to_j2("{%- for attribute, value in " f"{object}" ".attributes %}{% endfor -%}")
        ==
        "{%- for attribute, value in " f"{object}" ".attributes.items() %}{% endfor -%}"
    )


@pytest.mark.parametrize("template", (
    """\n    {% set describedBy = "" %}""",
    """\n    {% set describedBy = params.describedBy if params.describedBy else "" %}""",
    """\n    {% set describedBy = params.fieldset.describedBy if params.fieldset.describedBy else "" %}""",
))
def test_adds_nonlocal_namespace_if_template_includes_describedBy(template):
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


def test_adds_nonlocal_namespace_if_template_includes_anyRowHasActions():
    template = """{% set anyRowHasActions = false %}"""
    assert "{%- set nonlocal = namespace() -%}" in njk_to_j2(template)


def test_patches_anyRowHasActions_to_set_nonlocal():
    template = \
"""
{% set anyRowHasActions = false %}
{% set anyRowHasActions = true if row.actions.items else anyRowHasActions %}
{% elseif anyRowHasActions %}
"""
    assert (
        njk_to_j2(template)
        ==
"""
{%- set nonlocal = namespace() -%}
{% set nonlocal.anyRowHasActions = false %}
{% set nonlocal.anyRowHasActions = true if row.actions.items__njk else nonlocal.anyRowHasActions %}
{% elif nonlocal.anyRowHasActions %}
"""
    )


def test_adds_nonlocal_namespace_if_template_includes_isConditional():
    # govukRadios and govukCheckboxes both set describedBy before isConditional
    # so we should have nonlocal set via our describedBy patch
    template = """{% set describedBy = "" %}{% set isConditional = false %}"""
    assert "{%- set nonlocal = namespace() -%}" in njk_to_j2(template)


def test_patches_isConditional_to_set_nonlocal():
    template = \
"""
{% set isConditional = false %}
{% set isConditional = true %}
{%- if isConditional %} data-module="radios"{% endif -%}>
{%- if isConditional %} govuk-radios--conditional{% endif -%}
"""
    assert (
        njk_to_j2(template)
        ==
"""
{% set nonlocal.isConditional = false %}
{% set nonlocal.isConditional = true %}
{%- if nonlocal.isConditional %} data-module="radios"{% endif -%}>
{%- if nonlocal.isConditional %} govuk-radios--conditional{% endif -%}
"""
    )