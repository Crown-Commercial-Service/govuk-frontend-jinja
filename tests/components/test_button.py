from textwrap import dedent

from govuk_frontend.templates import Environment


def test_default_example():
    env = Environment()
    template = env.get_template("components/button/template.njk")

    assert (
        template.render(params={"text": "Save and continue"}).strip() == dedent(
            """
            <button type="submit" class="govuk-button">
              Save and continue
            </button>"""
        ).strip()
    )


def test_default_example_macro():
    env = Environment()
    template = env.from_string(dedent(
        """
        {% from "components/button/macro.njk" import govukButton %}

        {{ govukButton({
          "text": "Save and continue"
        }) }}"""
    ))
    assert (
        template.render().strip() == dedent(
        """
        <button type="submit" class="govuk-button">
          Save and continue
        </button>"""
        ).strip()
    )
