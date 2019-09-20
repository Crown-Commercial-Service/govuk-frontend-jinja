def test_fieldset(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)


def test_fieldset_with_block(env, similar, template, expected):
    template = env.from_string(template)
    assert similar(template.render(), expected)
