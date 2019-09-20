def test_header(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_service_name(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_service_name_and_navigation(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_header_with_service_name_and_navigation_and_autoescape(
    env, loader, file_factory, similar
):
    from govuk_frontend_jinja.templates import Environment

    env = Environment(autoescape=True, loader=loader)

    template = file_factory(
        "test_header_with_service_name_and_navigation", "t"
    ).read_text()
    expected = file_factory(
        "test_header_with_service_name_and_navigation", "x"
    ).read_text()

    template = env.from_string(template)
    assert similar(template.render(), expected)
