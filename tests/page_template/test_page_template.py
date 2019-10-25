import pytest

import govuk_frontend_jinja


@pytest.fixture
def env(loader):
    return govuk_frontend_jinja.Environment(
        # for some reason the page_template tests only pass with trim_blocks=False
        loader=loader,
        autoescape=True,
        keep_trailing_newline=True,
        trim_blocks=False,
        lstrip_blocks=True,
    )


def test_page_template(env, template, expected, similar):
    template = env.from_string(template)
    assert similar(template.render(), expected)
