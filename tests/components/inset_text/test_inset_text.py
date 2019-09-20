
import pytest


def test_inset_text(env):
    template = env.from_string(
"""
{% from "inset-text/macro.njk" import govukInsetText %}

{{ govukInsetText({
  "text": "It can take up to 8 weeks to register a lasting power of attorney if there are no mistakes in the application."
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-inset-text">
  It can take up to 8 weeks to register a lasting power of attorney if there are no mistakes in the application.
</div>
"""
        )
    )


def test_inset_text_with_html(env):
    template = env.from_string(
r"""
{% from "inset-text/macro.njk" import govukInsetText %}

{{ govukInsetText({
  "html": "It can take up to 8 weeks to register a <a class=\"govuk-link\" href=\"#\">lasting power of attorney</a> if there are no mistakes in the application."
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-inset-text">
  It can take up to 8 weeks to register a <a class="govuk-link" href="#">lasting power of attorney</a> if there are no mistakes in the application.
</div>
"""
        )
    )
