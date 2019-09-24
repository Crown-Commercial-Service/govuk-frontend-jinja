def test_tag(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_tag_inactive(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
