
from govuk_frontend.templates import Environment


def test_hint_template():
    env = Environment()
    template = env.get_template("components/hint/template.njk")
    assert (
        template.render(params={
            "text": "It’s on your National Insurance card, benefit letter, payslip or P60.\nFor example, ‘QQ 12 34 56 C‘.\n",
        })
        ==
"""<span class="govuk-hint">
  It’s on your National Insurance card, benefit letter, payslip or P60.
For example, ‘QQ 12 34 56 C‘.

</span>"""
    )


def test_hint():
    env = Environment()
    template = env.from_string(
"""{% from "components/hint/macro.njk" import govukHint %}

{{ govukHint({
  "text": "It’s on your National Insurance card, benefit letter, payslip or P60.\nFor example, ‘QQ 12 34 56 C‘.\n"
}) }}"""
    )
    assert (
        template.render()
        ==
"""

<span class="govuk-hint">
  It’s on your National Insurance card, benefit letter, payslip or P60.
For example, ‘QQ 12 34 56 C‘.

</span>"""
    )
