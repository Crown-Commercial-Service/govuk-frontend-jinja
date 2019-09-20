def test_details(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_details_with_html(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
