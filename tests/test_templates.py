
import pytest

from govuk_frontend.templates import njk_to_j2


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


@pytest.mark.parametrize(
    ("input, expected_output"),
    (
        ("{% ' ' + item if item %}", "{% ' ' + item if item else '' %}"),
        ("{% ' ' + (item if item) %}", "{% ' ' + (item if item else '') %}"),
        pytest.param("{% 'hello ' + (' world' if item) %}", "{% 'hello ' + (' world' if item else '') %}", marks=pytest.mark.xfail),
        ("{% ' ' + item if item else '' %}", "{% ' ' + item if item else '' %}"),
        ("{% ' ' + (item if item else '') %}", "{% ' ' + (item if item else '') %}"),
    ),
)
def test_adds_else_statement_to_inline_if_expressions(input, expected_output):
    assert njk_to_j2(input) == expected_output


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
