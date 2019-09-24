from textwrap import dedent


def test_default_example(env):
    template = env.get_template("components/button/template.njk")

    assert (
        template.render(params={"text": "Save and continue"}).strip()
        == dedent(
            """
            <button type="submit" class="govuk-button">
              Save and continue
            </button>"""
        ).strip()
    )


def test_default_example_macro(env):
    template = env.from_string(
        dedent(
            """
        {% from "components/button/macro.njk" import govukButton %}

        {{ govukButton({
          "text": "Save and continue"
        }) }}"""
        )
    )
    assert (
        template.render().strip()
        == dedent(
            """
        <button type="submit" class="govuk-button">
          Save and continue
        </button>"""
        ).strip()
    )


def test_disabled_button_macro(env):
    template = env.from_string(
        dedent(
            """
        {% from "button/macro.njk" import govukButton %}

        {{ govukButton({
          "text": "Disabled button",
          "disabled": true
        }) }}"""
        )
    )
    assert (
        template.render().strip()
        == dedent(
            """
        <button type="submit" disabled="disabled" aria-disabled="true" class="govuk-button govuk-button--disabled">
          Disabled button
        </button>"""
        ).strip()
    )


def test_link_button_macro(env):
    template = env.from_string(
        dedent(
            """
        {% from "button/macro.njk" import govukButton %}

        {{ govukButton({
          "text": "Link button",
          "href": "/",
        }) }}"""
        )
    )
    assert (
        template.render().strip()
        == dedent(
            """
        <a href="/" role="button" draggable="false" class="govuk-button">
          Link button
        </a>"""
        ).strip()
    )


def test_disabled_link_button_macro(env):
    template = env.from_string(
        dedent(
            """
        {% from "button/macro.njk" import govukButton %}

        {{ govukButton({
          "text": "Link button",
          "href": "/",
          "disabled": true
        }) }}"""
        )
    )
    assert (
        template.render().strip()
        == dedent(
            """
        <a href="/" role="button" draggable="false" class="govuk-button govuk-button--disabled">
          Link button
        </a>"""
        ).strip()
    )


def test_start_button_macro(env):
    template = env.from_string(
        dedent(
            """
        {% from "button/macro.njk" import govukButton %}

        {{ govukButton({
          "text": "Start now link button",
          "href": "/",
          "classes": "govuk-button--start"
        }) }}"""
        )
    )
    assert (
        template.render().strip()
        == dedent(
            """
        <a href="/" role="button" draggable="false" class="govuk-button govuk-button--start">
          Start now link button
        </a>"""
        ).strip()
    )


def test_input_button_macro(env):
    template = env.from_string(
        dedent(
            """
        {% from "button/macro.njk" import govukButton %}

        {{ govukButton({
          "element": "input",
          "name": "start-now",
          "text": "Start now"
        }) }}"""
        )
    )
    assert (
        template.render().strip()
        == """<input value="Start now" name="start-now" type="submit" class="govuk-button">"""
    )


def test_disabled_input_button_macro(env):
    template = env.from_string(
        dedent(
            """
        {% from "button/macro.njk" import govukButton %}

        {{ govukButton({
          "element": "input",
          "text": "Explicit input button disabled",
          "disabled": true
        }) }}"""
        )
    )
    assert template.render().strip() == (
        """<input value="Explicit input button disabled" type="submit" disabled="disabled" """
        """aria-disabled="true" class="govuk-button govuk-button--disabled">"""
    )
