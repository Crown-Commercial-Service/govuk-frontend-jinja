def test_tabs(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tabs_simple(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
