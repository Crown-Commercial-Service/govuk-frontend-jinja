def test_default(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_with_custom_text(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
