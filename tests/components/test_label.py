
import pytest

from textwrap import dedent

def test_default_example(env):
    template = env.get_template("components/label/template.njk")
    assert (
        template.render(params={
            "text": "National Insurance number",
        })
        ==
        dedent("""




        <label class="govuk-label">
          National Insurance number
        </label>


        """)
    )


def test_default_example_macro(env):
    template = env.from_string(dedent(
            """
            {% from "components/label/macro.njk" import govukLabel %}

            {{ govukLabel({
              "text": "National Insurance number"
            }) }}"""
    ))
    assert (
        template.render()
        ==
        dedent(
        """
        \n\n\n\n\n\n
        <label class="govuk-label">
          National Insurance number
        </label>\n\n\n""")
    )


def test_label_for(env):
    template = env.from_string(
"""
{% from "label/macro.njk" import govukLabel %}

{{ govukLabel({
  "text": "National Insurance number",
  "for": "label-example",
}) }}
"""
    )
    assert (
        template.render()
        ==
"""\n\n\n\n\n\n\n
<label class="govuk-label" for="label-example">
  National Insurance number
</label>\n\n
"""
    )


def test_label_with_undefined_params(env):
    template = env.from_string(
"""
{% from "label/macro.njk" import govukLabel %}

{{ govukLabel({
  "html": html,
  "text": "National Insurance number",
  "classes": classes,
  "isPageHeading": isPageHeading,
  "for": "label-example",
}) }}
"""
    )
    assert (
        template.render()
        ==
"""\n\n\n\n\n\n\n
<label class="govuk-label" for="label-example">
  National Insurance number
</label>\n\n
"""
    )
