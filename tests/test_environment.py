
from govuk_frontend.templates import Environment


def test_chainable_undefined():
    env = Environment()
    template = env.from_string("{{ item.hint.text }}")
    assert (
        template.render(item={"hint": {"text": "foobar"}})
        ==
        "foobar"
    )
    assert (
        template.render(item={"hint": {}})
        ==
        ""
    )
    assert (
        template.render(item={})
        ==
        ""
    )
    assert (
        template.render()
        ==
        ""
    )
