
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
